<script lang="ts">
    import { onMount } from "svelte";
    import { writable } from "svelte/store";
    import "bulma/css/bulma.css";

    const isActive = writable(false);

    onMount(() => {
        const navbarBurgers = Array.prototype.slice.call(
            document.querySelectorAll(".navbar-burger"),
            0,
        );

        navbarBurgers.forEach((el) => {
            el.addEventListener("click", () => {
                const target = el.dataset.target;
                const targetElement = document.getElementById(target);

                el.classList.toggle("is-active");
                isActive.update((value: any) => !value);
                if (targetElement) {
                    targetElement.classList.toggle("is-active");
                }
            });
        });

        // Cleanup function to remove event listeners
        return () => {
            navbarBurgers.forEach((el) => {
                el.removeEventListener("click");
            });
        };
    });
</script>

<nav class="navbar" aria-label="main navigation">
    <div class="navbar-brand">
        <a class="navbar-item" href="/">
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
</nav>

<slot />
