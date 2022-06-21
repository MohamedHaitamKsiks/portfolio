<script setup>
import MoonIcon from './MoonIconComponent.vue';

</script>

<template>
    <img v-if="avatar" src="../assets/images/profile2.png" :class="getClass" alt="Profile Picture" @click="onClick()" @mouseenter="hover=true" @mouseleave="hover=false"/>
    <img v-if="!avatar" src="../assets/images/real_profile.jpg" :class="getClass" alt="Profile Picture" @click="onClick()" @mouseenter="hover=true" @mouseleave="hover=false"/>

    <div class="moons-container" v-if="!$isMobile()">
        <MoonIcon v-for="(moon, i) in moonIcons" :src="moon" :rotationInit="i * 360 / moonIcons.length" ref="moonIcon"/>
    </div>
    
</template>

<script>
    export default {
        components: {
            MoonIcon
        },
        data() {
            return {
                avatar: true,
                onAnimation: false,
                moonIcons: [
                    'html5.png',
                    'css3.png',
                    'javascript.png',
                    'node-js.png',
                    'mysql.png',
                    'c.png',
                    'java.png',
                    'python.png',
                    'godot.png',
                    'git.png'
                ],
                radius: 0,
                hover: false,
                updateInterval: 0
                
            }
        },
        methods: {
            onClick() {
                if (!this.onAnimation) {
                    this.onAnimation = true;
                    this.avatar = !this.avatar;
                    this.radius = 0;
                    setTimeout(() => {
                        this.onAnimation = false;
                    }, 200)
                }
            },
            
        },
        computed: {
            getClass() {
                let animation = this.onAnimation ? ' animation-zoom': '';
                let newClass = 'profile-picture' + animation;
                //console.log(newClass);
                return newClass ;
            },
        },
        mounted () {
            //don't show planet on mobile

            this.updateInterval = setInterval(() => {
                if (this.$isMobile())
                    return;

                if (this.hover) 
                    this.radius = (15*this.radius + 300) / 16;
                else
                    this.radius = (15*this.radius + 240) / 16;
                
                for (let i = 0; i < this.moonIcons.length; i++){
                    this.$refs.moonIcon[i].radius.x = this.radius;
                    this.$refs.moonIcon[i].updatePosition()
                }   
            }, 10);
        },
        unmounted () {
            clearInterval(this.updateInterval);
        }
    }
</script>

<style>
    .profile-picture {
        width: 10%;
        height: 10%;
        min-width: 120px;
        min-height: 120px;
        max-width: 220px;
        max-height: 220px;
        margin: 100px;

        display: block;
        margin-left: auto;
        margin-right: auto;
        
        border-radius: 50%;
        box-shadow: 0px 8px 8px rgba(6, 10, 17, 0.51);
        transition: transform 0.3s;
        
    }

    .animation-zoom{
        animation-name: zoomIn;
        animation-duration: 0.2s;
    }

    .profile-picture:hover{
        transform: scale(1.1);
        cursor: pointer;
    }
    

    @keyframes zoomIn {
        0%{
            /*transform: rotate(0deg);*/
            transform: scale(0);
        }
        80% {
            transform: scale(1.1);
        }
        100%{
            transform: scale(1);
        }
    }

    .moons-container {
       
    }
    
</style>