<script setup>
    
    import skills from '../../public/skills.json';
    import SkillCategory from '../components/Skills/SkillCategoryComponent.vue';
</script>


<template>

    <div class="skills-container">

        <h1 class="project-div-title"> - My Skills - </h1>


        <SkillCategory v-for="(skillCategory, index) in skills" 
        :skills="skillCategory.skills" :title="skillCategory.category" :wait="index"/>

    </div>

</template>

<style>

    .skills-container {
        margin: 64px;
        margin-top: 160px;
    }


</style>