<script setup>
    import { RouterLink, RouterView } from 'vue-router'
    import NavbarLink from './NavbarLinkComponent.vue'
</script>

<template>
    <nav class="navbar">
        <NavbarLink href="/" value="Home" />
        <NavbarLink href="/projects" value="Projects" />
        <NavbarLink href="/freelance" value="Freelance" />
        <NavbarLink href="/about" value="About" />
        <NavbarLink href="/contact" value="Contact" />
    </nav>
</template>

<style>
	.navbar {
		background-color: var(--navbarcolor);
		padding: 20px;
		text-align: center;
        font-size: larger;
        box-shadow: 0px 8px 10px #010b1288;
        overflow: hidden;
        width: 100%;
        position: fixed;
        top: 0;
	}

</style>