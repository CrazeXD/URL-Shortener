<script>
    import { onMount } from "svelte";
    let current_url = "";
    onMount(() => current_url = window.location.href);
    // @ts-ignore
    async function handleSubmit(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        try {
            const response = await fetch("http://127.0.0.1:8000/api/shorten", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();

            if (result.error) {
                alert(result.error);
            } else {
                alert(`Shortened URL: ${current_url}${result.alias}`);
            }
        } catch (error) {
            console.error("Error:", error);
            alert("An error occurred while processing your request.");
        }
    }
</script>

<main>
    <div class="columns">
        <div class="column">
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
                <div class="container">
                    <form on:submit|preventDefault={handleSubmit}>
                        <p class="is-size-5 pb-2 changa">Your Long URL</p>
                        <div class="field has-addons">
                            <div class="control is-expanded">
                                <input
                                    class="input"
                                    type="url"
                                    name="url"
                                    placeholder="Enter a URL to shorten"
                                    required
                                />
                            </div>
                        </div>
                        <p class="is-size-5 pb-2 changa">
                            Your Custom Code <span class="has-text-danger"
                                >(optional)</span
                            >
                        </p>
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
                                <button
                                    class="button is-success has-text-color-black"
                                    type="submit"
                                >
                                    Shorten
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </section>
        </div>
        <div class="column"></div>
    </div>
</main>


<style>
    @import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap");
    @import url("https://fonts.googleapis.com/css2?family=Jura:wght@300..700&display=swap");
    @import url("https://fonts.googleapis.com/css2?family=Changa:wght@200..800&display=swap");

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
    .changa {
        font-family: "Changa", sans-serif;
        font-weight: 400;
    }
</style>

