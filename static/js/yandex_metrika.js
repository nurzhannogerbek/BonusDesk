(function (d, w, c) {
    (w[c] = w[c] || []).push(function () {
        try {
            w.yaCounter49431130 = new Ya.Metrika2({
                id: 49431130,
                clickmap: true,
                trackLinks: true,
                accurateTrackBounce: true,
                webvisor: true,
                trackHash: true,
                ut: "noindex",
                ecommerce: "dataLayer"
            });
        } catch (e) {
        }
    });
    var n = d.getElementsByTagName("script")[0], s = d.createElement("script"), f = function () {
        n.parentNode.insertBefore(s, n);
    };
    s.type = "text/javascript";
    s.async = true;
    s.src = "https://cdn.jsdelivr.net/npm/yandex-metrica-watch/tag.js";
    if (w.opera == "[object Opera]") {
        d.addEventListener("DOMContentLoaded", f, false);
    } else {
        f();
    }
})(document, window, "yandex_metrika_callbacks2");