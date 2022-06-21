<script setup>
</script>

<template>
    <img :src="'/icons/moons/' + src" class="moon-icon" :style="{left: position.x + 'px',top: position.y + 'px', 'z-index': position.z, width: size + 'px'}"/>
</template>

<script>
import { compileStyle } from '@vue/compiler-sfc';

export default {
    expose: ['updatePosition','position','rotation', 'radius'],
    props: {
        src: String,
        rotationInit: Number
    },
    data() {
        return {
            //position
            position: {
                x: 0,
                y: 0,
                z: 0
            },
            //rotation
            rotation: 5.0,
            //circle radius
            radius: {
                x: 240,
                y: 70,
                rotation: 0.0
            },
            size: 48
        }
    },
    methods: {
        updatePosition() {    
            //position
            this.position.x = this.radius.x * Math.cos(this.rotation) + window.innerWidth / 2 - 48;
            this.position.y = this.radius.y * Math.sin(this.rotation) + 240;

            //radius rotation
            this.size = 48 + 12 * Math.sin(this.rotation) 
            //this.radius.y = 20 + 60 * Math.cos(this.radius.rotation)


            //z index
            if (this.rotation > Math.PI)
                this.position.z = -10;
            else
                this.position.z = 10;

            //update rotation
            this.rotation += 0.009;
            this.radius.rotation -= 0.005;
            if (this.rotation > 2 * Math.PI)
                this.rotation -= 2 * Math.PI;
                
            //console.log(this.position)
        }
    },
    mounted() {
        this.rotation = Math.PI * this.rotationInit / 180.0;
       
    }
}
</script>

<style>
    .moon-icon {
        width: 48px;
        border-radius: 50%;
        background-color: rgb(255, 255, 255);
        position: absolute;
        opacity: 100%;
        pointer-events:  none;
        box-shadow: -2px 2px 2px 2px rgba(5, 12, 22, 0.311);
        
    }
</style>