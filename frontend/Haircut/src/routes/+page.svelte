<script lang="ts">
    import "bulma/css/bulma.css";

    function submitForm(event: Event) {
        event.preventDefault();
        const form = event.target as HTMLFormElement;
        const formData = new FormData(form);
        fetch("http://127.0.0.1:8000/api/shorten", {
            method: "POST",
            body: formData,
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.error) {
                    alert(data.error);
                } else {
                    alert(`Shortened URL: ${data.shortened}`);
                }
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }
</script>

<nav class="navbar" aria-label="main navigation">
    <div class="navbar-brand">
        <a class="navbar-item" href="http://127.0.0.1:8000/">
            <img src="/favicon.png" alt="Logo" />
        </a>

        <!-- svelte-ignore a11y-missing-attribute -->
        <a
            role="button"
            class="navbar-burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbar"
        >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
        </a>
    </div>

    <div id="navbar" class="navbar-menu">
        <div class="navbar-start">
            <a class="navbar-item" href="http://127.0.0.1:8000/"> Home </a>
            <a class="navbar-item" href="/about"> API </a>
            <a class="navbar-item" href="/contact"> Contact </a>
            <a href="/pricing" class="navbar-item"> Pricing </a>
        </div>

        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                    <a class="button is-primary" href="http://127.0.0.1:8000/signup">
                        <strong>Sign up</strong>
                    </a>
                    <a class="button is-light" href="http://127.0.0.1:8000/login"> Log in </a>
                </div>
            </div>
        </div>
    </div>
</nav>

<main>
    <section class="section">
        <div class="container">
            <h1
                class="title has-text-primary playfair"
                style="margin-bottom: 8px;"
            >
                Haircut
            </h1>
            <p class="subtitle jura">A free URL shortener.</p>
        </div>
        <br />
        <div class="columns">
            <div class="column">
                <div class="container">
                    <form method="post" action="">
                        <div class="field has-addons">
                            <div class="control is-expanded">
                                <input
                                    class="input"
                                    type="url"
                                    name="url"
                                    placeholder="Enter a URL to shorten"
                                />
                            </div>
                        </div>
                        <div class="field has-addons">
                            <div class="control is-expanded">
                                <input
                                    type="text"
                                    name="alias"
                                    class="input"
                                    placeholder="Enter an alias"
                                />
                            </div>
                        </div>
                        <div class="field has-text-aligned-center">
                            <div class="control">
                                <button class="button is-primary" type="submit">
                                    Shorten
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</main>

<style>
    @import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap");
    @import url("https://fonts.googleapis.com/css2?family=Jura:wght@300..700&display=swap");
    .title {
        font-size: 3rem;
    }
    .subtitle {
        font-size: 1.5rem;
    }
    .playfair {
        font-family: "Playfair Display", serif;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
    }
    .jura {
        font-family: "Jura", sans-serif;
        font-weight: 300;
    }
</style>
