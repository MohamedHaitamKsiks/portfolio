<script setup>
import IconComponent from './IconComponent.vue';

</script>

<template>
    <img :class="getArrowClass" src="../assets/icons/down_arrow.png"/>
    <div class="footer">
        
        <nav class="icon-list">
            <IconComponent href="https://github.com/MohamedHaitamKsiks" src="/src/assets/icons/github_icon.png" delay="0s"/>
            <IconComponent href="https://github.com/MohamedHaitamKsiks" src="/src/assets/icons/fiverr_icon.png"  delay="1s"/>
            <IconComponent href="https://github.com/MohamedHaitamKsiks" src="/src/assets/icons/linkedin_icon.png"  delay="2s"/>
            <IconComponent href="https://github.com/MohamedHaitamKsiks" src="/src/assets/icons/itch_io_icon.png"  delay="3s"/>
        </nav>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                scrolled: false
            }
        },
        mounted() {
            window.addEventListener("scroll", this.onScroll);
        },
        methods: {
            onScroll() {
                this.scrolled = window.scrollY != 0;
            }
        },
        computed: {
            getArrowClass() {
                let animation = !this.scrolled ? '' : ' down-arrow-fade';
                return 'down-arrow' + animation;
            }
        }
    }
</script>

<style>
    .footer {
        position: absolute;
        left: 0px;
        right: 0px;

        padding: 32px;
        margin: 12px;
        height: 120px;

        border-top-style: solid;
        border-top-width: 2px;

        margin-top: 10%;
        
    }
    .icon-list {
        text-align: center;
    }
    .down-arrow {
        width: 4%;

        position: fixed;
        bottom: 32px;
        left: 47%;

        transition: opacity 0.3s;
        
        
    }


    .down-arrow-fade {
        opacity: 0%;
    }

</style>