<section class="hero is-fullheight-with-navbar">
    <div class="hero-body">
        <div class="container">
            <div class="columns is-flex-direction-column is-justify-content-center">
                <div class="column is-5-desktop is-offset-3-desktop">
                    <div class="box">
                        <h1 class="title has-text-centered jura">Log In</h1>
                        <form class="form">
                            <!--on:submit|preventDefault={handleSubmit}-->
                            <div class="field">
                                <label class="label changa" for="username">Username</label>
                                <div class="control" id="username">
                                    <input
                                        class="input"
                                        type="text"
                                        name="username"
                                        placeholder="Enter your username"
                                        maxlength="20"
                                        required
                                    />
                                </div>
                            </div>
                            <div class="field">
                                <label class="label changa" for="password">Password</label>
                                <div class="control" id="password">
                                    <input
                                        class="input"
                                        type="password"
                                        name="password"
                                        placeholder="Enter your password"
                                        required
                                    />
                                </div>
                            </div>
                            <div class="field changa">
                                <div class="control has-text-centered">
                                    <button class="button is-success" type="submit">Sign Up</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<style>
    @import url("https://fonts.googleapis.com/css2?family=Jura:wght@300..700&display=swap");
    @import url("https://fonts.googleapis.com/css2?family=Changa:wght@200..800&display=swap");

    .title {
        font-size: 3rem;
    }
    .subtitle {
        font-size: 1.5rem;
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