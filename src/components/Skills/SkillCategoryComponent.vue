<script setup>
    import SkillComponent from './SkillComponent.vue';   
</script>

<template>
    <div :class="className">
        <div class="skill-category-container-title">
            {{ title }}
        </div>

        <div class="skill-category-container-body">
            <SkillComponent v-for="(skill, index) in skills" 
            :skill="skill.skill" :value="skill.value" 
            :wait="100 * index + 500 * wait + 100"/>
        </div>

    </div>
</template>

<script>
    export default {
        props: {
            skills: Array,
            title: String,
            wait: Number
        },
        data() {
            return {
                className: "skill-category-container skill-category-container-hidden"
            }
        },
        mounted() {
            setInterval(() => {
                this.className = 'skill-category-container';
            }, 500 * this.wait);
        }
    }
</script>

<style>
    .skill-category-container {
        margin: auto;
        margin-top: 1cm;
        width: 55%;
        padding: 0%;

        background-color: var(--navbarcolor);
        border-radius: 0.5cm;
        overflow: hidden;
        transition:  all 0.6s;
        transform: translateX(0cm);
    }

    .skill-category-container-hidden {
        transform: translateX(-5cm);
        opacity: 0%;
    }

    .skill-category-container-title {
        background-color: rgba(37, 37, 37, 0.771);
        padding: 0.5cm;
        text-align: center;
        font-size: larger;
    }

    .skill-category-container-body {
        padding: 0.5cm;
    }

</style>