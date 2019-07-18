<template>
    <div id="date-time">
        <div class="date">{{date}}</div>
        <div class="time">{{HM}}
            <span class="second">{{second}}</span>
            <span>{{timeTag=='下午'?'PM':'AM'}}</span>
        </div>
    </div>
</template>

<script>
    import moment from 'moment'

    export default {
        name: "DateTime",
        data() {
            return {
                date: '',
                HM: '',
                second: '',
                timeTag: ''
            }
        },
        methods: {
            getTime(){
                this.date = moment().format('MMM Do YYYY')
                this.HM = moment().format('h:mm')
                this.second = moment().format('ss')
                this.timeTag = moment().format('a')
            },
            updateTime() {
                setInterval(() => {
                    this.getTime()
                }, 1000)
            }

        },
        computed: {},
        created() {
            moment.locale('zh-cn');
        },
        mounted() {
            this.getTime()
            this.updateTime()
        }

    }
</script>

<style scoped lang="scss">
    .date {
        font-size: .5rem;
    }

    .time {
        font-size: .5rem;

        .second {
            font-size: .25rem;
        }
    }
</style>
