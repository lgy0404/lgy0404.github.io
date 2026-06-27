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

  .author__name {
    white-space: nowrap;
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
    align-items: center;
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
  .exp-logo {
    width: auto;
    height: 1.1em;
    margin: 0 0.25em 0 0.1em;
    vertical-align: -0.18em;
  }
  .exp-logo--kuaishou {
    height: 1.2em;
    vertical-align: -0.24em;
  }
  .exp-logo--vivo {
    height: 0.85em;
    vertical-align: -0.08em;
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

I am a Ph.D. candidate in the Department of Control Science and Engineering at Zhejiang University (ZJU), where I have been since 2023, under the supervision of [Prof. Yong Liu](https://person.zju.edu.cn/yongliu), [Prof. Jiangning Zhang](https://zhangzjn.github.io/), and [Dr. Liang Liu](https://scholar.google.com/citations?user=Kkg3IPMAAAAJ&hl=en) at the [ZJU APRIL Lab](https://april.zju.edu.cn/). My research explores the foundations of **universal digital agents**: intelligent systems that can understand digital environments, adapt to new tasks, and assist people across apps, devices, and software workflows.

<div class="profile-stats" markdown="1">

**Citations:** <a href="https://scholar.google.com/citations?user=XqQp-fkAAAAJ&hl=zh-CN"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-375-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10"></a> <a href="https://scholar.google.com/citations?user=XqQp-fkAAAAJ&hl=zh-CN"><img alt="First-author citations" src="https://img.shields.io/badge/First--Author-107-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10"></a> **First-Author Stars:** <a href="https://github.com/lgy0404"><img alt="First-author project stars" src="https://img.shields.io/badge/First--Author%20Stars-582-white?logo=GitHub&style=flat-square&labelColor=white&logoColor=black&cacheSeconds=10"></a>

</div>

<span class='anchor' id='news'></span>
# 🔥 News

<div class="news-scroll" markdown="1">

- *2026.06*: Released [MemGUI-Agent](https://memgui-agent.github.io/), an end-to-end long-horizon mobile GUI agent with proactive context management.
- *2026.06*: Released [MobileForge](https://mobile-forge.github.io/), an annotation-free adaptation system for mobile GUI agents.
- *2026.05*: Recognized as a Silver Reviewer for ICML 2026.
- *2026.04*: [LearnAct](https://lgy0404.github.io/LearnAct/) has been accepted by ACL 2026.
- *2026.02*: Released [MemGUI-Bench](https://lgy0404.github.io/MemGUI-Bench/), a memory-centric benchmark for mobile GUI agents in dynamic environments.
- *2025.10*: Our survey, [LLM-Powered GUI Agents in Phone Automation](https://arxiv.org/abs/2504.19838), appears at TMLR.
- *2025.04*: Released [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838).
- *2025.04*: Released [LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://arxiv.org/abs/2504.13805).

</div>

<span class='anchor' id='selected-work'></span>
# 📝 Selected Work

<div class="paper-card">
  <div class="paper-card__image">
    <div class="paper-card__thumb">
      <span class="paper-card__badge paper-card__badge--venue">Preprint</span>
      <a href="https://arxiv.org/abs/2606.19926">
        <img src="./images/paper-images/memgui-agent-conact.png" alt="MemGUI-Agent ConAct framework">
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
    <div class="paper-card__links"><a href="https://github.com/kwai/MemGUI-Agent"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/kwai/MemGUI-Agent?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
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
    <div class="paper-card__links"><a href="https://github.com/kwai/MobileForge"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/kwai/MobileForge?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
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
    <div class="paper-card__links"><a href="https://github.com/lgy0404/MemGUI-Bench"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/lgy0404/MemGUI-Bench?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a> <a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=17604234699666112827,6880181861836555417"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-11-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
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
    <div class="paper-card__links"><a href="https://github.com/lgy0404/LearnAct"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/lgy0404/LearnAct?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a> <a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=15460424372315407973"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-36-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
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
      <li>Provides a systematic map of LLM-powered mobile GUI agents, covering frameworks, models, data, evaluation, and open challenges.</li>
      <li>Clarifies how phone automation is moving from static scripts toward perception-reasoning-action agents.</li>
    </ul>
    <div class="paper-card__links"><a href="https://github.com/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a> <a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=6050737529106194091,847899513706501378"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-60-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a></div>
  </div>
</div>

## Selected Collaborations

- [**UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning**](https://ojs.aaai.org/index.php/AAAI/article/view/38816) \
<span style="font-size: 0.93em;"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Han Xiao, Shuai Ren, Pengxiang Zhao, **<u>Guangyi Liu</u>**, Guanjing Xiong, and Hongsheng Li.</span>\
<span style="font-size: 0.93em;"><img src="./images/logo-venue.png" style="width: 0.975em; position: relative; top: -0.115em;"> **AAAI 2026**</span>\
<a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=13436621043121462425,11490050979982859007"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-195-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a>

- [**A3: Android Agent Arena for Mobile GUI Agents**](https://openreview.net/forum?id=zE2tVigoub) \
<span style="font-size: 0.93em;"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> Yuxiang Chai, Shunye Tang, Han Xiao, Weifeng Lin, Liang Liu, Hanhao Li, Jiayu Zhang, Pengxiang Zhao, **<u>Guangyi Liu</u>**, Rongduo Han, Guozhi Wang, Shuai Ren, Siyuan Huang, and Hongsheng Li.</span>\
<span style="font-size: 0.93em;"><img src="./images/logo-venue.png" style="width: 0.975em; position: relative; top: -0.115em;"> **ACL 2026 Findings**</span>\
<a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=14530162543617210928,7058152315375786309"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-42-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a>

- [**FedGUI: Benchmarking Federated GUI Agents across Heterogeneous Platforms, Devices, and Operating Systems**](https://arxiv.org/abs/2604.14956) \
<span style="font-size: 0.93em;"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> Wenhao Wang, Haoting Shi, Mengying Yuan, Yiquan Lin, Panrong Tong, Hanzhang Zhou, **<u>Guangyi Liu</u>**, Pengxiang Zhao, Yue Wang, and Siheng Chen.</span>\
<span style="font-size: 0.93em;"><img src="./images/logo-venue.png" style="width: 0.975em; position: relative; top: -0.115em;"> **ACL 2026 Findings**</span>\
<a href="https://github.com/wwh0411/FedGUI"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/wwh0411/FedGUI?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a>

- [**UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization**](https://arxiv.org/abs/2604.13822) \
<span style="font-size: 0.93em;"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> Zhengxi Lu, Fei Tang, **<u>Guangyi Liu</u>**, Kaitao Song, Xu Tan, Jin Ma, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, and Yongliang Shen.</span>\
<span style="font-size: 0.93em;"><img src="./images/logo-venue.png" style="width: 0.975em; position: relative; top: -0.115em;"> **ACL 2026 Main**</span>

- [**MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents**](https://arxiv.org/abs/2509.06477) \
<span style="font-size: 0.93em;"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> Pengxiang Zhao, **<u>Guangyi Liu</u>**, Yaozhen Liang, Weiqing He, Zhengxi Lu, Yuehao Huang, Yaxuan Guo, Kexin Zhang, Hao Wang, Liang Liu, and Yong Liu.</span>\
<span style="font-size: 0.93em;"><img src="./images/logo-venue.png" style="width: 0.975em; position: relative; top: -0.115em;"> **ACL 2026 Main**</span>\
<a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=9453730861622247470"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-4-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a>

- [**FedMABench: Benchmarking Mobile GUI Agents on Decentralized Heterogeneous User Data**](https://aclanthology.org/2025.emnlp-main.1341/) \
<span style="font-size: 0.93em;"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> Wenhao Wang, Zijie Yu, Rui Ye, Jianqing Zhang, **<u>Guangyi Liu</u>**, Liang Liu, Siheng Chen, and Yanfeng Wang.</span>\
<span style="font-size: 0.93em;"><img src="./images/logo-venue.png" style="width: 0.975em; position: relative; top: -0.115em;"> **EMNLP 2025 Main (Oral)**</span>\
<a href="https://github.com/wwh0411/FedMABench"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/wwh0411/FedMABench?style=flat-square&logo=github&logoColor=black&labelColor=white&color=white&label=Stars&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a> <a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=4859074859912844261"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-10-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a>

- [**MobileA3gent: Training Mobile GUI Agents Using Decentralized Self-Sourced Data from Diverse Users**](https://aclanthology.org/2025.hcinlp-1.8/) \
<span style="font-size: 0.93em;"><img src="./images/logo-author.png" style="width: 1em; position: relative; top: -0.1em;"> Wenhao Wang, Mengying Yuan, Zijie Yu, **<u>Guangyi Liu</u>**, Rui Ye, Tian Jin, Siheng Chen, and Yanfeng Wang.</span>\
<span style="font-size: 0.93em;"><img src="./images/logo-venue.png" style="width: 0.975em; position: relative; top: -0.115em;"> **CFAgentic @ ICML 2025 (Oral)**</span>\
<a href="https://scholar.google.com/scholar?oi=bibs&hl=en&cites=10794877405588499537,10796259486820381126"><img alt="Google Scholar citations" src="https://img.shields.io/badge/Citations-13-white?logo=Google%20Scholar&style=flat-square&labelColor=white&cacheSeconds=10" style="border: 1px solid #ccc; border-radius: 4px;"></a>

<span class='anchor' id='education'></span>
# 📖 Education

- 2025.09 - Present | <img src="./images/logos/zju-logo-1.png" class="edu-logo" alt="Zhejiang University logo"> Ph.D. Student, Zhejiang University, Hangzhou  
  Advisors: [Prof. Yong Liu](https://person.zju.edu.cn/yongliu), [Prof. Jiangning Zhang](https://zhangzjn.github.io/), and [Dr. Liang Liu](https://scholar.google.com/citations?user=Kkg3IPMAAAAJ&hl=en); [ZJU APRIL Lab](https://april.zju.edu.cn/).
- 2023.06 - 2025.08 | <img src="./images/logos/zju-logo-1.png" class="edu-logo" alt="Zhejiang University logo"> M.S. Student, Zhejiang University, Hangzhou  
  Advisor: [Prof. Wenchao Meng](https://person.zju.edu.cn/wmeng); [ZJU NeSC Group](http://nesc.zju.edu.cn/).
- 2019.09 - 2023.06 | <img src="./images/logos/cumt-logo.png" class="edu-logo edu-logo--cumt" alt="China University of Mining and Technology logo"> B.Eng. in Automatic Control, China University of Mining and Technology, Xuzhou  
  Advisor: [Prof. Wei Dai](https://faculty.cumt.edu.cn/DaiW/zh_CN/img/175786/list/%7B%7B:linkUrl%7D%7D); Ranking: No.1/203 overall; National Scholarship recipient.

<span class='anchor' id='experiences'></span>
# 💻 Experiences

- 2025.08 - Present | <img src="./images/logos/kuaishou-icon.png" class="exp-logo exp-logo--kuaishou" alt="Kuaishou logo"> Kuaishou Technology  
  Research Intern; Mentor: [Martin Li](https://scholar.google.com/citations?user=atSPcL8AAAAJ&hl=zh-CN).
- 2024.08 - 2025.08 | <img src="./images/logos/vivo-logo.svg" class="exp-logo exp-logo--vivo" alt="vivo logo"> vivo AI Lab  
  Research Intern; Mentors: [Dr. Liang Liu](https://scholar.google.com/citations?user=Kkg3IPMAAAAJ&hl=en) and [Prof. Hongsheng Li](https://www.ee.cuhk.edu.hk/~hsli/).

# 🏆 Honors & Awards

- Silver Reviewer, ICML 2026.
- Excellent Graduate Student of Zhejiang University.
- Excellent Student Cadre of Zhejiang University.
- National Scholarship, 2020 and 2021.

# 🎓 Academic Service

- **Reviewer (Conferences):** ICLR, NeurIPS, ICML, ECCV, ACM MM, EMNLP.
- **Reviewer (Journals):** TMLR.

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
