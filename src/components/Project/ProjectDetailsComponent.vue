<script setup>
    import ToolsComponent from './ToolsComponent.vue'
</script>


<template>
    <div class="project-details-container">
        <div class="project-details">
            
            <div class="project-details-images-comtainer">

                <div class="project-images-buttons-container"
                    :style="{ 'background-image': 'url(' + getImagePath +')' }">

                    <img src="/icons/left-arrow.png" class="project-images-button"
                        v-if="currentImage > 0" @click="currentImage--" />
                    <img src="/icons/right-arrow.png" class="project-images-button" style="left: 100%;"
                        v-if="currentImage < project.images.length - 1" @click="currentImage++" />

                </div>

            </div>

            <div class="project-details-description">
                <h3 style="padding: 16px; border-bottom-style: solid; border-bottom-width: 1px; width: 80%; ">
                    # {{ project.title }}
                </h3>
                <br />

                <i style="opacity: 60%">
                    /*
                    <p> &ensp; {{ project.type }}</p>
                    <p> &ensp; date : {{ project.year }}</p>
                    */
                </i>

                <p
                    style="padding-bottom: 16px; padding-top: 16px; border-bottom-style: solid; border-bottom-width: 1px; width: 90%; white-space: pre-wrap;">
                    <strong>description: </strong> <br /><br />
                    &ensp; {{ project.description }}
                </p>
                <br />
                <strong>tools: </strong> <br />
                <ToolsComponent :tools="project.tools" />

                <div style="width: 100%; height: auto; ">
                    <button style="position: sticky; left: 100%;" class="button-primary"
                        @click="$emit('back')">Back</button>
                </div>
            </div>


        </div>
    </div>
</template>


<script>

    export default {
        props: {
            project: Object,
        },
        emits: [
            "back"
        ],
        data() {
            return {
                currentImage: 0
            };
        },
        methods: {

        }, 
        computed: {
            getImagePath() {
                return "'/projects/images" + '/' + this.project.id + '/' + this.project.images[this.currentImage] + "'";
            },
            getNextImagePath() {
                return "'/projects/images" + '/' + (this.project.id + 1) + '/' + this.project.images[this.currentImage] + "'";
            },
            getPrevImagePath() {
                return "'/projects/images" + '/' + (this.project.id - 1) + '/' + this.project.images[this.currentImage] + "'";
            }
        }
    }
</script>


<style>
    /*project details container*/
    .project-details-container {
        /*position*/
        position: fixed;
        left: 0;
        top: 0;
        z-index: 1000;

        /*size*/
        width: 100%;
        height: 100%;

        /*blur background*/
        backdrop-filter: blur(2px);
        background-color: rgba(0, 0, 0, 0.305);
        box-shadow: 0 16px 16px 16px rgba(0, 0, 0, 0.47);  
        
    }

    /* project details */
    .project-details {
        /*box*/
        background-color:  rgb(5, 9, 17);
        position: fixed;
        left: 10%;
        top: 10%;

        width: 80%;
        height: 80%;

        min-width: 30cm;
        
        /*border*/
        border-radius: 0.4cm;
        overflow: hidden;

    }



    /* container of all images */
    .project-details-images-comtainer {
        /* box size */
        width: 70%;
        height: 100%;
        overflow: hidden;
        background-color: black;

    }

    /* buttons container */
    .project-images-buttons-container {
        width: 100%;
        height: 100%;
        background-size: contain;
        background-repeat: no-repeat;
        background-position-y: center;
        background-position-x: center;
    }

    /* image buttons */
    .project-images-button {
        width: 1.5cm;
        position: sticky;
        top: 50%;
        opacity: 60%;
        filter: drop-shadow(0 0.2cm 0.1cm rgba(0, 0, 0, 0.916));
        transition: all 0.2s;
    }

    .project-images-button:hover {
        cursor: pointer;
        opacity: 100%;
    }


    .project-details-description {
        /* position */
        position: relative;
        left: 70%;
        bottom: 100%;

        /* box */
        width: 30%;
        height: 100%;
        
        /* padding */
        padding: 0.5cm;

        overflow: scroll;
    }

</style>