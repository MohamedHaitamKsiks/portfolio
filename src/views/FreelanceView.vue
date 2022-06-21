<script setup>
    import ReviewCard from '../components/Review/ReviewCardComponent.vue';
    import fiverrReviews from '../../public/reviews/fiverrReviews.json'
</script>

<template>
    <div class="reviews-div">
        <h1 class="project-div-title"> - My Fiverr Reviews - </h1>

        <ReviewCard v-for="(review, index) in reviews" :review="review" :wait="index * 250" />
    </div>
</template>

<script>
    export default {
        data() {
            return {
                reviews: []
            }
        },
        mounted() {
            this.reviews = fiverrReviews.sort((a, b) => 0.5 - Math.random()); 
        }
    }
</script>

<style>
    .reviews-div {
        margin: 0.5cm;
        margin-top: 160px;
    }
</style>