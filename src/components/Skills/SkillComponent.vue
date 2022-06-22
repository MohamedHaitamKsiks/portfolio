
<template>
    <div :class="className">
        <div class="skill-title">
            {{ skill }}
        </div>
        <div class="skill-value-container">
            <div class="skill-value" :style="{width: currentValue}">
                
            </div>
        </div>
    </div>

</template>

<script>
    export default {
        props: {
            skill: String,
            value: Number,
            wait: Number
        },
        data() {
            return {
                currentValue: '0%',
                className: 'skill-container skill-container-hidden'
            }
        },
        mounted() {
            //show
            setTimeout(() => {
                //charge bar
                setTimeout(() => {
                    this.currentValue = this.value + '%';
                }, 100);
                this.className = 'skill-container';
            }, this.wait + 10);
        }
    }
</script>

<style>
    /* skill container */
    .skill-container {
        display: flex;
        flex: auto;
        width: 100%;
        margin-top: 0.5cm;
        transition: all 0.3s;
        transform: translateX(0cm);
    }

    .skill-container-hidden {
        opacity: 0%;
    }

    .skill-title {
        width: 20%;
        display: inline-block;
        font-size: larger;
        font-weight: bolder;
        margin-right: 0.5cm;
        color: var(--focuscolor);
    }
    

    .skill-value-container {
        display: inline-flex;
        flex: auto;
        background-color: rgba(39, 39, 39, 0.61);
        width: 5cm;
        height: 0.5cm;
        text-align: center;
        border-radius: 0.5cm;
    }


    .skill-value {
        background-color: var(--focuscolor);
        width: 0%;
        height: 100%;
        transition: width 0.8s;
        border-radius: 0.5cm;
    }

</style>


