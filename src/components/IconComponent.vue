
<template>
    <a :href="href" class="icon-link"><img :src="'/icons/' + src" class="icon-image" /></a>
</template>


<script>
    //define icon args
    export default{
        props: {
            href: String,
            src: String,
        },
        
    }
</script>

<style>
    .icon-image {
        width: 64px;
        margin: 32px;
        margin-left: 3%;
        margin-right: 3%;
        animation-name: animation-icon;
        animation-duration: 5s;
        animation-iteration-count: infinite;
    }

    @keyframes animation-icon {
        0% {
            transform: scale(1);
        }
        50% {
           transform: scale(1.15);
        }
        100% {
            transform: scale(1);
        }
    }
</style>