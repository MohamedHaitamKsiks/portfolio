
<template>
    <div :class="className">
        <div class="review-card-header">
            <!--img src="/icons/star.png"/-->
            <img :src="review.client.picture" class="review-card-client-picture" />
            <div class="review-card-client-info">
                <div class="review-card-client-name">
                    {{ review.client.name }}
                </div>
                <div class="review-card-client-country"> 
                    // {{ review.client.country }} 
                </div>
            </div>
            <img src="/icons/star.png" class="review-card-stars" />
            <h2 class="review-card-stars">
                {{ review.stars }}
            </h2>
        </div>
        <div class="review-card-comment">
            {{ review.comment }}
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            review: Object,
            wait: Number
        },
        data() {
            return {
                className: 'review-card'
            }
        },
        mounted() {
            setTimeout(() => {
                this.className = 'review-card review-card-show'
            }, this.wait)
        }
    }
</script>

<style>
    /*card body*/
    .review-card {
        margin: auto;
        margin-top: 1cm;
        /*width: 11cm;*/
        width: 60%;
        min-width: 12cm;
        background-color: rgb(18, 24, 32);
        border-radius: 0.3cm;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.673);
        transition: all 0.7s;
        opacity: 0%;
        transform: translateX(-5cm);
    }

    .review-card-show {
        opacity: 100%;
        transform: translateY(0cm);
    }

    /*header*/
    .review-card-header {
        padding: 0.5cm;
        width: 100%;
    }

    /* review card client info */

    .review-card-client-picture {
        display: inline-flex;
        width: 2.5cm;
        border-radius: 100%;
        vertical-align: middle;
    }

    .review-card-client-info {
        display: inline-block;
        vertical-align: middle;
        margin-left: 0.5cm;
        margin-right: 1cm;
    }

    .review-card-client-name {
        display: flex;
        flex: auto;
        font-size: larger;
        font-weight: 700;
        
    }

    .review-card-client-country {
        display: flex;
        flex: auto;
        opacity: 60%;
        margin-top: 0.2cm;
    }

    .review-card-stars {
        display: inline-flex;
        vertical-align: middle;
        margin-left: 0.5cm;
        color: #FAB005;
    }

    /*footer*/
    .review-card-comment {
        padding: 0.5cm ;
        /*border-top-color:  white;
        border-top-style: solid;*/
        margin: auto;
    }

    /*project title*/
    .review-card-title {
        text-align: center;
    }



</style>