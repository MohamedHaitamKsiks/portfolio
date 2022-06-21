<script setup></script>

<template>
    <div class="not-found-container">
        <h1>404</h1> <br/> <br/>
        <h3>Page not found!</h3>
    </div>
</template>

<script>
    export default {
        mounted() {
            window.scrollTo(0, 0);
        }
    }
</script>

<style>
    .not-found-container {
        text-align: center;
        margin: 64px;
        margin-top: 160px;
    }
</style>