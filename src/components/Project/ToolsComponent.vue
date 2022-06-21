<template> 
    <div class="project-card-tools">
        <div v-for="tool in tools" class="tool-container">{{ tool }}</div>
    </div>
</template>

<script>
    export default {
        props: {
            tools: Array,
        }
    }
</script>

<style>
    .project-card-tools {
        width: 100%;
    }

    /*project tool*/
    .tool-container {
        border-style: solid;
        border-width: 1px;
        border-color: rgba(255, 255, 255, 0.592);
        border-radius: 0.5cm;

        padding: 0.25cm;
        padding-top: 0.1cm;
        padding-bottom: 0.1cm;

        margin: 0.1cm;

        width:fit-content;
        text-align: center;
        opacity: 50%;
        background-color: rgba(12, 18, 21, 0.668);

        display: inline-block;
    }
</style>