<script setup>
	import { RouterLink, RouterView } from 'vue-router';
	import Navbar from './components/Navbar/NavbarComponent.vue';
	import Footer from './components/FooterComponent.vue';

</script>

<template>
	<header>
		<Navbar/>
	</header>

	<RouterView />
	

	<Footer/>
	
</template>

<style>

</style>