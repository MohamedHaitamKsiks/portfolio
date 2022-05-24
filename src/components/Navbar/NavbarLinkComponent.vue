<script setup>
    import { RouterLink, useRoute } from 'vue-router'
</script>

<template>
    <RouterLink :to="{ path: href }" :class="getClass">{{ value }}</RouterLink>
</template>

<script>
    export default {
        props: {
            href: String,
            value: String
        },
        data(){
            return {
                focusClass: 'router-link router-link-focus',
                baseClass: 'router-link',
            }
        },
        computed: {
            getClass() {
                console.log(this.href);
                return useRoute().path===this.href ? this.focusClass:this.baseClass;
            }
        },
        
    }
</script>

<style>
    .router-link {
		color: white;
        text-decoration: none;
		padding: 2%;
        padding-bottom: 16px;

        border-bottom-style: solid;
        border-color: #f66b0e00;

        transition: color 0.3s, border-color 0.3s;
	}

    .router-link-focus {
        border-bottom-style: solid;
        border-bottom-width: 3px;
        border-color: var(--focuscolor);
        color: var(--focuscolor);
        
    }

    .router-link:hover{
        border-bottom-width: 3px;
        border-color: var(--focuscolor);
        color: var(--focuscolor);
    }
</style>