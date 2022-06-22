<script setup>
    import { RouterLink, RouterView } from 'vue-router'
    import NavbarLink from './NavbarLinkComponent.vue'
</script>

<template>
    <nav class="navbar">
        <NavbarLink href="/" value="About" />
        <NavbarLink href="/skills" value="Skills" />
        <NavbarLink href="/projects" value="Projects" />
        <NavbarLink href="/freelance" value="Freelance" />
    </nav>
</template>

<style>
	.navbar {
		background-color: var(--navbarcolor);
		padding: 20px;
		text-align: center;
        font-size: larger;
        box-shadow: 0px 8px 10px #010b1288;
        overflow:auto;
        width: 100%;
        position: fixed;
        top: 0;

        z-index: 100;
	}

</style>