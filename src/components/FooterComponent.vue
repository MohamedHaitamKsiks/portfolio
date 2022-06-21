<script setup>
import IconComponent from './IconComponent.vue';

</script>

<template>
    <img v-if="canScroll" :class="getArrowClass" src="/icons/down_arrow.png" />
    <div class="footer">
        <h2>My Socials</h2>
        <nav class="icon-list">
            <IconComponent href="https://github.com/MohamedHaitamKsiks" src="github_icon.png" />
            <IconComponent href="https://www.fiverr.com/haitamksiks" src="fiverr_icon.png" />
            <IconComponent href="https://www.linkedin.com/in/mohamed-haitam-ksiks-58a56921a/" src="linkedin_icon.png" />
            <IconComponent href="https://simple-team.itch.io/" src="itch_io_icon.png" />
        </nav>
    </div>
</template>

<script>
    //down arrow code
    export default {
        data() {
            return {
                scrolled: false,
                canScroll: true
            }
        },
        mounted() {
            window.addEventListener("scroll", this.onScroll);
            this.canScroll = document.body.scrollHeight > document.body.clientHeight;
        },
        methods: {
            onScroll() {
                this.scrolled = window.scrollY > 64;
            },
            onResize() {
                this.canScroll = document.body.scrollHeight > document.body.clientHeight;
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

        text-align: center;
        /*border-top-style: solid;
        border-top-width: 2px;*/

        margin-top: 9%;
        
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