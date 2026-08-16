(function () {
  "use strict";

  const paperBadges = Array.from(
    document.querySelectorAll(".hf-download-badge[data-hf-paper-id]")
  );
  const totalBadges = Array.from(
    document.querySelectorAll(".hf-download-badge[data-hf-total]")
  );
  const allBadges = [...paperBadges, ...totalBadges];
  if (!allBadges.length) return;

  const collectionsUrl = "https://huggingface.co/api/collections?owner=lgy0404&limit=100";
  const modelsUrl =
    "https://huggingface.co/api/models?author=lgy0404&limit=100&expand=downloadsAllTime";
  const datasetsUrl =
    "https://huggingface.co/api/datasets?author=lgy0404&limit=100&expand=downloadsAllTime";
  const compactNumber = new Intl.NumberFormat("en-US", {
    notation: "compact",
    maximumFractionDigits: 1,
  });
  const exactNumber = new Intl.NumberFormat("en-US");

  function fetchJson(url) {
    return fetch(url, { headers: { Accept: "application/json" }, cache: "no-store" })
      .then((response) => {
        if (!response.ok) throw new Error(`Hugging Face API returned ${response.status}`);
        return response.json();
      });
  }

  function resourceLabel(count, singular, plural) {
    return `${count} ${count === 1 ? singular : plural}`;
  }

  function updateBadge(badge, downloads, modelCount, datasetCount) {
    const value = badge.querySelector(".hf-download-badge__value");
    const resources = [];

    if (modelCount) resources.push(resourceLabel(modelCount, "model", "models"));
    if (datasetCount) resources.push(resourceLabel(datasetCount, "dataset", "datasets"));

    const exactDownloads = exactNumber.format(downloads);
    const breakdown = resources.length ? ` across ${resources.join(" and ")}` : "";
    const description = `${exactDownloads} all-time downloads${breakdown}`;

    value.textContent = compactNumber.format(downloads).toLowerCase();
    badge.title = description;
    badge.setAttribute("aria-label", `Hugging Face: ${description}`);
    badge.dataset.state = "live";
  }

  allBadges.forEach((badge) => {
    badge.dataset.state = "loading";
  });

  Promise.all([fetchJson(collectionsUrl), fetchJson(modelsUrl), fetchJson(datasetsUrl)])
    .then(([collections, models, datasets]) => {
      const resourcesByPaper = new Map();
      const allResources = new Map();
      const downloadsByResource = new Map();

      models.forEach((item) => {
        downloadsByResource.set(`model:${item.id}`, Number(item.downloadsAllTime) || 0);
      });
      datasets.forEach((item) => {
        downloadsByResource.set(`dataset:${item.id}`, Number(item.downloadsAllTime) || 0);
      });

      collections.forEach((collection) => {
        const items = Array.isArray(collection.items) ? collection.items : [];
        const paperIds = items
          .filter((item) => item.type === "paper")
          .map((item) => String(item.id));
        const resources = items.filter(
          (item) => item.type === "model" || item.type === "dataset"
        );

        paperIds.forEach((paperId) => {
          if (!resourcesByPaper.has(paperId)) resourcesByPaper.set(paperId, new Map());
          const paperResources = resourcesByPaper.get(paperId);

          resources.forEach((item) => {
            const key = `${item.type}:${item.id}`;
            const resource = { id: item.id, type: item.type };
            paperResources.set(key, resource);
            allResources.set(key, resource);
          });
        });
      });

      function summarize(resources) {
        const entries = Array.from(resources.entries());
        if (!entries.length || entries.some(([key]) => !downloadsByResource.has(key))) {
          return null;
        }

        const values = entries.map(([, resource]) => resource);
        return {
          downloads: entries.reduce(
            (sum, [key]) => sum + downloadsByResource.get(key),
            0
          ),
          modelCount: values.filter((item) => item.type === "model").length,
          datasetCount: values.filter((item) => item.type === "dataset").length,
        };
      }

      paperBadges.forEach((badge) => {
        const resources = resourcesByPaper.get(badge.dataset.hfPaperId);
        const summary = resources ? summarize(resources) : null;

        if (!summary) {
          badge.dataset.state = "fallback";
          return;
        }

        updateBadge(
          badge,
          summary.downloads,
          summary.modelCount,
          summary.datasetCount
        );
      });

      const totalSummary = summarize(allResources);
      totalBadges.forEach((badge) => {
        if (!totalSummary) {
          badge.dataset.state = "fallback";
          return;
        }

        updateBadge(
          badge,
          totalSummary.downloads,
          totalSummary.modelCount,
          totalSummary.datasetCount
        );
      });
    })
    .catch(() => {
      allBadges.forEach((badge) => {
        badge.dataset.state = "fallback";
      });
    });
})();
