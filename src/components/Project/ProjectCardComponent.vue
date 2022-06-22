<script setup>
import ToolsComponent from './ToolsComponent.vue';

</script>

<template>


    <div :class="'project-card ' + getHideClass">
        <div class="project-card-header">
            // {{ project.type }}
        </div>

        <img class="project-card-image" :src="imagePath"/>

        <div class="project-card-footer">
            <h3 class="project-card-title">
                {{ project.title }} 
                <a :href="project.link" class="project-card-link" target=”_blank”>
                    <img src="/icons/link_icon.png" width="24" @mouseenter="linkHover=true" @mouseleave="linkHover=false" style="position: relative; top: 0.125cm"/><br/>
                    <div :class="'project-link-hover ' + getHoverClass"> {{ project.link }}</div>
                </a>
            </h3>

            <ToolsComponent :tools = "project.tools"/>

            <span class="project-card-more-container">
                <button class="button-primary project-card-more" @click="$emit('show-details', project)">Details</button>
            </span>
        </div>
    </div>
</template>


<script>
    export default {
        props: {
            project: Object,
            wait: Number
        },
        emits: ['show-details'],
        data() {
            return {
                linkHover: false,
                imagePath: '',
                visible: false
            }
        },
        mounted() {
            this.imagePath = '/projects/images/' + this.project.id + '/' + this.project.images[this.project.main];
            setTimeout(() => {
                this.visible = true;
            }, this.wait * 100 + 10)
        },
        computed: {
            getHoverClass(){
                return this.linkHover ? 'project-link-hover-fadein' : '';
            },
            getHideClass() {
                return this.visible ? 'project-card-show' : '';
            }
        }
    }
</script>

<style>


    /*card body*/
    .project-card {
        margin: 12px;
        display: inline-block;
        /*width: 11cm;*/
        width: 12cm;
        background-color: rgb(18, 24, 32);
        border-radius: 0.3cm;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.673);
        transition: all 0.7s;
        opacity: 0%;
        transform: translateY(5cm);
    }

    .project-card-show {
        opacity: 100%;
        transform: translateY(0cm);
    }

    /*header*/
    .project-card-header {
        text-align: left;
        opacity: 60%;
        padding: 0.2cm;
    }

    /*image class*/
    .project-card-image {
        /*image size*/
        width: inherit;
        height: 9cm;
        object-fit:cover;
        background-color: black;
        
    }

    /*footer*/
    .project-card-footer {
        padding: 0.5cm;
        padding-top: 0cm;
    }

    /*project title*/
    .project-card-title{
        text-align: center;
    }

    /*project link*/
    .project-link-hover {
        position: absolute;

        margin-left: 0.3cm;

        padding: 0.3cm  ;
        background-color: white;
        border-radius: 0.5cm;

        opacity: 0%;

        font-size: small;
        color: black;

        transition: opacity 0.6s;
        z-index: 100;

    }

    .project-link-hover-fadein {
        opacity: 70%;
    }

    /*projec more button*/
    .project-card-more-container {
        width: 100%;
    }

    .project-card-more {
        /*position*/
        position: sticky;
        left: 100%;
    }

</style>