<script setup>
import ProfilePicture from "../components/ProfilePictureComponent.vue";
    
</script>

<template>
	<section class="home-section">
        <ProfilePicture />
        <div class="name-container">
            <p class="name">KSIKS MOHAMED HAITAM</p>
            <p class="job">/*{{ text }}{{ writing }}*/</p>
        </div>
        <div class="description-container">
            <p>
                Hello, My name is Ksiks Mohamed Haitam. I'm a software engineer student and a part time game developer.
                I've worked with many clients providing all sorts of develomenent sercives.
                <br/> 
            </p>
            <p>
                This portfolio contains all the informations you need regarding my skills, experiences and projects.
                It was built using HTML, CSS, JavaSript and VueJS.
            </p>
        </div>
    </section>
</template>


<script>
    export default {
        data() {
            return {
                job: ' software engineer ',
                text: '',
                position: 0,
                writing: ''
            }
        },
        mounted() {
            //start writing
            setTimeout(this.addCharacter(), 1100);
            this.writing = '_'
        },
        methods: {
            addCharacter() {
                if (this.position < this.job.length){
                    let char = this.job[this.position];
                    //speed depends on the character
                    if (char == ' ')
                        setTimeout(this.addCharacter, 20)
                    else
                        setTimeout(this.addCharacter, 90)
                    //write character
                    this.text += char;
                    this.position++;
                }
                if (this.position == this.job.length) {
                    this.writing='';
                }
            }
        }
        
    }
</script>

<style>
    .home-section {
        margin: 32px;
        margin-top: 160px;
        width: auto;
    }
    .name-container {
        text-align: center;
        font-weight: 100;
        margin: 32px;
        
    }

    .name {
        margin: 16px;
        font-size: 64px;
        text-shadow: 0px 8px 8px rgba(6, 10, 18, 0.515);
    }

    .job {
        font-size: 32px;
        color: rgba(255, 255, 255, 0.495);
    }


    .description-container{
        text-align: justify; 
        padding-left: 30%;
        padding-right: 30%;
        margin-top: 48px;
        margin-bottom: 48px;
        
    }

</style>