---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
  .page__content a,
  .page__content a:hover,
  .page__content a:focus,
  .page__content a:visited {
    text-decoration: none;
  }

  .author-more {
    display: inline;
  }
  .author-more .author-toggle {
    display: none;
  }
  .author-more .more-label,
  .author-more .author-rest {
    color: #888;
    text-decoration: underline dotted;
    text-underline-offset: 2px;
  }
  .author-more .more-label {
    display: inline;
    margin: 0;
    cursor: pointer;
  }
  .author-more .author-rest {
    display: none;
    margin: 0;
    cursor: pointer;
  }
  .author-more .author-toggle:checked + .more-label {
    display: none;
  }
  .author-more .author-toggle:checked ~ .author-rest {
    display: inline;
  }

  .paper-card {
    display: flex;
    align-items: flex-start;
    gap: 1.5rem;
    padding: 1.25rem 0;
    border-bottom: 1px solid #ececec;
  }
  .paper-card:first-of-type {
    padding-top: 0.5rem;
  }
  .paper-card__image {
    flex: 0 0 min(42%, 380px);
    max-width: 380px;
  }
  .paper-card__thumb {
    position: relative;
  }
  .paper-card__image a {
    display: block;
  }
  .paper-card__image img {
    display: block;
    width: 100%;
    height: auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    background: #fff;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  }
  .paper-card__badge {
    position: absolute;
    top: 7px;
    left: -10px;
    z-index: 1;
    padding: 0.28rem 0.75rem;
    border-radius: 0;
    color: #fff;
    font-size: 0.78em;
    font-weight: 700;
    line-height: 1.2;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
  }
  .paper-card__badge--venue {
    background: #113fa8;
  }
  .paper-card__badge--preprint {
    background: #666;
  }
  .paper-card__content {
    flex: 1 1 auto;
    min-width: 0;
  }
  .paper-card__title {
    margin: 0 0 0.35rem;
    font-size: 1.05em;
    line-height: 1.45;
  }
  .paper-card__meta {
    font-size: 0.98em;
    line-height: 1.7;
  }
  .paper-card__venue {
    font-size: 0.98em;
    line-height: 1.7;
  }
  .paper-card__links {
    margin-top: 0.2rem;
    font-size: 0.93em;
    line-height: 1.7;
  }
  .paper-card__highlights {
    margin: 0.55rem 0 0;
    padding-left: 1.2rem;
    font-size: 0.95em;
    color: #444;
  }
  .paper-card__highlights li {
    margin-bottom: 0.35rem;
  }
  .news-scroll {
    max-height: 21rem;
    overflow-y: auto;
    overflow-x: hidden;
    padding-right: 0.75rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 12px -14px rgba(0, 0, 0, 0.35);
  }
  .news-scroll ul {
    margin-bottom: 0;
  }
  .profile-stats img {
    border: 1px solid #ccc;
    border-radius: 4px;
    margin: 0 0.15rem 0.2rem 0;
    vertical-align: middle;
  }
  .edu-logo {
    width: auto;
    height: 1.35em;
    margin-right: 0.25em;
    vertical-align: -0.22em;
  }
  .edu-logo--cumt {
    height: 1.25em;
  }
  @media (max-width: 900px) {
    .paper-card {
      flex-direction: column;
      gap: 1rem;
    }
    .paper-card__image {
      flex-basis: auto;
      max-width: 100%;
      width: 100%;
    }
  }
</style>

<span class='anchor' id='about-me'></span>
# About me

I am a Ph.D. student at [Zhejiang University](https://www.zju.edu.cn/), working on **mobile GUI agents**, **multimodal large language models**, and **long-horizon agent learning**. My research asks how large multimodal models can perceive mobile interfaces, reason over user goals, remember task-relevant facts, and safely complete real app workflows.

I was a research intern at [vivo AI Lab](https://www.vivo.com/) from 2024.08 to 2025.08, and I am a research intern at [Kuaishou Technology](https://www.kuaishou.com/) from 2026.08 to present. I received my bachelor's degree from China University of Mining and Technology in 2023 and joined Zhejiang University for graduate study in 2023 before officially becoming a Ph.D. student in 2025.09.

<div class="profile-stats" markdown="1">

**Citations:** <a href="https://scholar.google.com/citations?user=XqQp-fkAAAAJ&hl=zh-CN"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-375-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10"></a> <a href="https://scholar.google.com/citations?user=XqQp-fkAAAAJ&hl=zh-CN"><img alt="First-author citations" src="https://img.shields.io/badge/First--Author-107-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10"></a> **First-Author Stars:** <a href="https://github.com/lgy0404"><img alt="First-author project stars" src="https://img.shields.io/badge/First--Author%20Stars-582-white?logo=GitHub&style=flat-square&labelColor=white&logoColor=black&cacheSeconds=10"></a>

</div>

**Research Interests:**
- **Mobile GUI Agents:** building agents that operate real phone apps through screenshots, UI state, and executable actions.
- **Agent Memory and Long-Horizon Control:** evaluating and improving short-term memory, long-term learning, and proactive context management.
- **Annotation-Free Adaptation:** converting self-collected app interaction and feedback into policy-improvement signals.
- **Demonstration Learning:** using a few human demonstrations to personalize agents for long-tail mobile workflows.

I aim to build **reliable mobile agents** that can connect language, vision, memory, action, and feedback under real-world constraints.

<span class='anchor' id='news'></span>
# 🔥 News

<div class="news-scroll" markdown="1">

- *2026.06*: Released [MemGUI-Agent](https://memgui-agent.github.io/), an end-to-end long-horizon mobile GUI agent with proactive context management.
- *2026.06*: Released [MobileForge](https://mobile-forge.github.io/), an annotation-free adaptation system for mobile GUI agents.
- *2026.02*: Released [MemGUI-Bench](https://lgy0404.github.io/MemGUI-Bench/), a memory-centric benchmark for mobile GUI agents in dynamic environments.
- *2026*: [LearnAct](https://lgy0404.github.io/LearnAct/) has been accepted by ACL 2026.
- *2025*: Our survey, [LLM-Powered GUI Agents in Phone Automation](https://arxiv.org/abs/2504.19838), appears at TMLR.
- *2024.08*: Joined vivo AI Lab as a research intern working on Phone GUI Agents.

</div>

<span class='anchor' id='experiences'></span>
# 💻 Experiences

- 2026.08 - Present | Kuaishou Technology  
  Research Intern on mobile GUI agents, annotation-free adaptation, and long-horizon context management.
- 2024.08 - 2025.08 | vivo AI Lab  
  Research Intern on Phone GUI Agents, few-shot demonstration learning, online evaluation, and memory-centric benchmarking.
- 2024.01 - 2024.05 | TruthAI  
  R&D intern on industrial large-model plugins and domain-specific model adaptation.

<span class='anchor' id='selected-work'></span>
# 📝 Selected Work

<div class="paper-card">
  <div class="paper-card__image">
    <div class="paper-card__thumb">
      <span class="paper-card__badge paper-card__badge--venue">Preprint</span>
      <a href="https://arxiv.org/abs/2606.19926">
        <img src="./images/paper-images/memgui-agent-teaser.png" alt="MemGUI-Agent teaser">
      </a>
    </div>
  </div>
  <div class="paper-card__content">
    <p class="paper-card__title"><a href="https://arxiv.org/abs/2606.19926"><strong>MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management</strong></a></p>
    <div class="paper-card__meta"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> <strong><u>Guangyi Liu</u></strong>, Gao Wu, Congxiao Liu, Pengxiang Zhao, Liang Liu, <span class="author-more"><input type="checkbox" id="author-more-0" class="author-toggle"><label for="author-more-0" class="more-label">5 More Authors</label><label for="author-more-0" class="author-rest"> Mading Li, Zhang Qi, Mengyan Wang, Liang Guo, and Yong Liu.</label></span></div>
    <ul class="paper-card__highlights">
      <li>Introduces Context-as-Action (ConAct), making history folding, UI memory, and step self-description first-class policy actions.</li>
      <li>Builds MemGUI-3K with 2,956 fully annotated trajectories and achieves strong long-horizon results on MemGUI-Bench and MobileWorld.</li>
    </ul>
    <div class="paper-card__links"><a href="https://memgui-agent.github.io/">Project</a> · <a href="https://arxiv.org/abs/2606.19926">Paper</a> · <a href="https://github.com/kwai/MemGUI-Agent"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/kwai/MemGUI-Agent?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
  </div>
</div>

<div class="paper-card">
  <div class="paper-card__image">
    <div class="paper-card__thumb">
      <span class="paper-card__badge paper-card__badge--venue">Preprint</span>
      <a href="https://arxiv.org/abs/2606.19930">
        <img src="./images/paper-images/mobileforge-main-performance.png" alt="MobileForge main performance">
      </a>
    </div>
  </div>
  <div class="paper-card__content">
    <p class="paper-card__title"><a href="https://arxiv.org/abs/2606.19930"><strong>MobileForge: Annotation-Free Adaptation for Mobile GUI Agents with Hierarchical Feedback-Guided Policy Optimization</strong></a></p>
    <div class="paper-card__meta"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> <strong><u>Guangyi Liu</u></strong>, Pengxiang Zhao, Gao Wu, Yiwen Yin, Mading Li, <span class="author-more"><input type="checkbox" id="author-more-1" class="author-toggle"><label for="author-more-1" class="more-label">6 More Authors</label><label for="author-more-1" class="author-rest"> Liang Liu, Congxiao Liu, Zhang Qi, Mengyan Wang, Liang Guo, and Yong Liu.</label></span></div>
    <ul class="paper-card__highlights">
      <li>Proposes MobileGym and HiFPO to connect target-app exploration, curriculum mining, rollout feedback, and policy optimization.</li>
      <li>Improves both generalist and GUI-specialized agents; ForgeOwl-8B reaches 77.6% Pass@3 on AndroidWorld and 41.0% on MobileWorld GUI-only.</li>
    </ul>
    <div class="paper-card__links"><a href="https://mobile-forge.github.io/">Project</a> · <a href="https://arxiv.org/abs/2606.19930">Paper</a> · <a href="https://github.com/kwai/MobileForge"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/kwai/MobileForge?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
  </div>
</div>

<div class="paper-card">
  <div class="paper-card__image">
    <div class="paper-card__thumb">
      <span class="paper-card__badge paper-card__badge--venue">Preprint</span>
      <a href="https://arxiv.org/abs/2602.06075">
        <img src="./images/paper-images/memgui-bench-overview.png" alt="MemGUI-Bench overview">
      </a>
    </div>
  </div>
  <div class="paper-card__content">
    <p class="paper-card__title"><a href="https://arxiv.org/abs/2602.06075"><strong>MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments</strong></a></p>
    <div class="paper-card__meta"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> <strong><u>Guangyi Liu</u></strong>, Pengxiang Zhao, Yaozhen Liang, Qinyi Luo, Shunye Tang, <span class="author-more"><input type="checkbox" id="author-more-2" class="author-toggle"><label for="author-more-2" class="more-label">10 More Authors</label><label for="author-more-2" class="author-rest"> Yuxiang Chai, Weifeng Lin, Han Xiao, WenHao Wang, Siheng Chen, Zhengxi Lu, Gao Wu, Hao Wang, Liang Liu, and Yong Liu.</label></span></div>
    <ul class="paper-card__highlights">
      <li>Builds a memory-centric benchmark with 128 tasks across 26 apps, where 89.8% challenge memory through cross-temporal and cross-spatial retention.</li>
      <li>Introduces MemGUI-Eval and reveals substantial memory gaps across 11 mobile GUI agents.</li>
    </ul>
    <div class="paper-card__links"><a href="https://lgy0404.github.io/MemGUI-Bench/">Project</a> · <a href="https://arxiv.org/abs/2602.06075">Paper</a> · <a href="https://github.com/lgy0404/MemGUI-Bench"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/lgy0404/MemGUI-Bench?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a> <a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=17604234699666112827,6880181861836555417"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-11-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
  </div>
</div>

<div class="paper-card">
  <div class="paper-card__image">
    <div class="paper-card__thumb">
      <span class="paper-card__badge paper-card__badge--venue">ACL 2026</span>
      <a href="https://arxiv.org/abs/2504.13805">
        <img src="./images/paper-images/learnact-teaser.png" alt="LearnAct teaser">
      </a>
    </div>
  </div>
  <div class="paper-card__content">
    <p class="paper-card__title"><a href="https://arxiv.org/abs/2504.13805"><strong>LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark</strong></a></p>
    <div class="paper-card__meta"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> <strong><u>Guangyi Liu</u></strong>, Pengxiang Zhao, Liang Liu, Zhiming Chen, Yuxiang Chai, <span class="author-more"><input type="checkbox" id="author-more-3" class="author-toggle"><label for="author-more-3" class="more-label">4 More Authors</label><label for="author-more-3" class="author-rest"> Shuai Ren, Hao Wang, Shibo He, and Wenchao Meng.</label></span></div>
    <div class="paper-card__venue"><img src="./images/logo-venue.png" style="width: 0.975em; position: relative; top: -0.115em;"> <strong>ACL 2026</strong></div>
    <ul class="paper-card__highlights">
      <li>Introduces LearnGUI with 2,252 offline tasks and 101 online tasks for demonstration-based learning.</li>
      <li>Designs DemoParser, KnowSeeker, and ActExecutor to extract, retrieve, and execute with human demonstration knowledge.</li>
    </ul>
    <div class="paper-card__links"><a href="https://lgy0404.github.io/LearnAct/">Project</a> · <a href="https://arxiv.org/abs/2504.13805">Paper</a> · <a href="https://github.com/lgy0404/LearnAct"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/lgy0404/LearnAct?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a> <a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=15460424372315407973"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-36-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
  </div>
</div>

<div class="paper-card">
  <div class="paper-card__image">
    <div class="paper-card__thumb">
      <span class="paper-card__badge paper-card__badge--venue">TMLR</span>
      <a href="https://arxiv.org/abs/2504.19838">
        <img src="./images/paper-images/survey-framework.png" alt="Phone GUI agent survey taxonomy">
      </a>
    </div>
  </div>
  <div class="paper-card__content">
    <p class="paper-card__title"><a href="https://arxiv.org/abs/2504.19838"><strong>LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects</strong></a></p>
    <div class="paper-card__meta"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> <strong><u>Guangyi Liu</u></strong>, Pengxiang Zhao, Yaozhen Liang, Liang Liu, Yaxuan Guo, <span class="author-more"><input type="checkbox" id="author-more-4" class="author-toggle"><label for="author-more-4" class="more-label">16 More Authors</label><label for="author-more-4" class="author-rest"> Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, WenHao Wang, Tianze Wu, Zhengxi Lu, Siheng Chen, LiLinghao, Hao Wang, Guanjing Xiong, Yong Liu, and Hongsheng Li.</label></span></div>
    <div class="paper-card__venue"><img src="./images/logo-venue.png" style="width: 0.975em; position: relative; top: -0.115em;"> <strong>TMLR</strong></div>
    <ul class="paper-card__highlights">
      <li>Provides a systematic map of LLM-powered phone GUI agents, covering frameworks, models, data, evaluation, and open challenges.</li>
      <li>Clarifies how phone automation is moving from static scripts toward perception-reasoning-action agents.</li>
    </ul>
    <div class="paper-card__links"><a href="https://arxiv.org/abs/2504.19838">Paper</a> · <a href="https://github.com/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a> <a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=6050737529106194091,847899513706501378"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-60-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
  </div>
</div>

<span class='anchor' id='education'></span>
# 📖 Education

- 2025.09 - Present | <img src="./images/logos/zju-logo-1.png" class="edu-logo" alt="Zhejiang University logo"> Ph.D. Student, Zhejiang University, Hangzhou  
  Research focus: mobile GUI agents, multimodal LLMs, agent memory, and policy adaptation.
- 2023.06 - 2025.08 | <img src="./images/logos/zju-logo-1.png" class="edu-logo" alt="Zhejiang University logo"> Graduate Student, Zhejiang University, Hangzhou  
  Research focus: LLM-powered agents and mobile GUI automation.
- 2019.09 - 2023.06 | <img src="./images/logos/cumt-logo.png" class="edu-logo edu-logo--cumt" alt="China University of Mining and Technology logo"> B.Eng. in Automatic Control, China University of Mining and Technology, Xuzhou  
  Ranking: No.1/203 overall; National Scholarship recipient.

# 🏆 Honors & Awards

- Excellent Graduate Student of Zhejiang University.
- Excellent Student Cadre of Zhejiang University.
- Silver Medal, China International "Internet+" Innovation and Entrepreneurship Competition.
- National Scholarship, 2020 and 2021.

<div id="footer" style="text-align: center; font-size: 0.9em; color: #666;">
  <br>
  <div class="site-traffic" style="color: #666; font-weight: 600;">
    <span id="busuanzi_container_site_pv">Total Views: <span id="busuanzi_value_site_pv"></span></span>
    <span style="color: #999;"> | </span>
    <span id="busuanzi_container_site_uv">Unique Visitors: <span id="busuanzi_value_site_uv"></span></span>
  </div>
</div>

<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>

<br>
