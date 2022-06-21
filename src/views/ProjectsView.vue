<script setup>
    import projects from '../../public/projects/projects.json'
import ProjectCardComponent from '../components/Project/ProjectCardComponent.vue';
import ProjectDetailsComponent from '../components/Project/ProjectDetailsComponent.vue';
</script>

<template>
    <div class="projects-div">

        <h1 class="project-div-title"> - Projects - </h1>
        
        <ProjectCardComponent v-for="(project, index) in sortedProjects" :project="project" :wait="index" @show-details="onShowDetails"/>
        <ProjectDetailsComponent v-if="onProjectDetails" @back="onHideDetails" ref="projectDetails" :project="currentProject" :class="'project-details-fade ' + projectDetailsClass" />

    </div>
</template>

<script>
    export default {
        data() {
            return {
                onProjectDetails: false,
                currentProject: projects[0],
                projectDetailsClass: '',
                sortedProjects: []
            }
        },
        mounted() {
            //sort projects
            this.sortedProjects = projects.sort((a, b) => {
                if (a.year > b.year)
                    return -1;
                else if (a.year == b.year)
                    return 0;
                else
                    return 1;
            })
            window.scrollTo(0, 0);
            console.log(projects);
        },
        methods: {
            onShowDetails(project) {
                console.log(project);
                //show deltail
                this.currentProject = project;
                this.onProjectDetails = true;
                //fade in
                setTimeout(() => {
                    this.projectDetailsClass = 'project-details-fadein';
                }, 10);
            },
            onHideDetails() {
                this.projectDetailsClass = '';
                setTimeout(() => {
                    this.onProjectDetails = false;
                }, 500);

            }
        }
    }
</script>

<style>
    .projects-div {
        /*height: 1000px;*/
        
        margin: 64px;
        margin-top: 160px;
    }

    .project-details-fade {
        transition: opacity 0.5s;
        opacity: 0%;
    }


    .project-details-fadein {
        opacity: 100%;
    }

    .project-div-title {
        text-align: center;
        margin-bottom: 64px;
        padding: 16px;
        border-bottom-color: white;
        border-bottom-style: solid;
        border-width: 2px;
        width: 50%;
        position: relative;
        left: 25%;
}

</style>