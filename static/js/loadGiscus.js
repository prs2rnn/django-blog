(function () {
  const btn = document.getElementById("discussion-details");
  if (btn) {
    btn.addEventListener(
      "click",
      () => {
        const container = document.getElementById("discussion");

        container.innerHTML = `
        <div id="giscus-container"></div>
      `;

        const script = document.createElement("script");

        script.src = "https://giscus.app/client.js";
        script.async = true;
        script.crossOrigin = "anonymous";

        script.setAttribute("data-repo", "prs2rnn/django-blog");
        script.setAttribute("data-repo-id", "R_kgDOSz8S0Q");
        script.setAttribute("data-category", "Posts");
        script.setAttribute("data-category-id", "DIC_kwDOSz8S0c4C_FZ_");
        script.setAttribute("data-mapping", "pathname");
        script.setAttribute("data-strict", "0");
        script.setAttribute("data-reactions-enabled", "1");
        script.setAttribute("data-emit-metadata", "0");
        script.setAttribute("data-input-position", "bottom");
        script.setAttribute("data-theme", "preferred_color_scheme");
        script.setAttribute("data-lang", "en");

        document.getElementById("giscus-container").appendChild(script);
      },
      { once: true },
    );
  }
})();
