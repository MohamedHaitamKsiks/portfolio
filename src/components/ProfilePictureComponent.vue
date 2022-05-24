<template>
    <img v-if="avatar" src="../assets/images/profile2.png" :class="getClass" alt="Profile Picture" @click="onClick()"/>
    <img v-if="!avatar" src="../assets/images/real_profile.jpg" :class="getClass" alt="Profile Picture" @click="onClick()" />
</template>

<script>
    export default {
        data() {
            return {
                avatar: true,
                onAnimation: false
                
            }
        },
        methods: {
            onClick() {
                if (!this.onAnimation) {
                    this.onAnimation = true;
                    this.avatar = !this.avatar;
                    setTimeout(() => {
                        this.onAnimation = false;
                    }, 200)
                }
            }
        },
        computed: {
            getClass() {
                let animation = this.onAnimation ? ' animation-zoom': '';
                let newClass = 'profile-picture' + animation;
                //console.log(newClass);
                return newClass ;
            },
        }
    }
</script>

<style>
    .profile-picture {
        width: 220px;
        height: 220px;
        margin: 80px;

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

    
</style>