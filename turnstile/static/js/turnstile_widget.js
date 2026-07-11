(
    function (fn) {
        if (document.readyState !== "loading") {
            fn()
        } else {
            document.addEventListener("DOMContentLoaded", fn)
        }
    }
)(
    turnstile.ready(
        function () {
            const load = function (container) {
                const inputName = container.getAttribute("data-wagtail-turnstile-input")
                const appearance = container.getAttribute("data-wagtail-turnstile-appearance")
                const siteKey = container.getAttribute("data-wagtail-turnstile-site-key")
                const input = container.parentNode.querySelector('input[name="' + inputName + '"]')
                const form = input ? input.closest("form") : null
                const disabledInputs = []

                const disableButtons = function () {
                    form.querySelectorAll('button[type="submit"], input[type="submit"]').forEach(
                        function (btn) {
                            if (!btn.disabled) {
                                disabledInputs.push(btn)
                                btn.disabled = true
                            }
                        }
                    )
                }

                const enableButtons = function () {
                    while (disabledInputs.length) {
                        disabledInputs.pop().disabled = false
                    }
                }

                const callback = function (token) {
                    if (input) {
                        input.value = token
                    }
                }

                if (!input && !form) {
                    console.error("No input found for name \"" + inputName + "\"")
                    return
                }

                turnstile.render(
                    container,
                    {
                        "appearance": appearance,
                        "sitekey": siteKey,
                        "before-interactive-callback": disableButtons,
                        "after-interactive-callback": enableButtons,
                        "callback": callback
                    }
                )
            }

            document.querySelectorAll("[data-wagtail-turnstile-input]").forEach(load)
        }
    )
)
