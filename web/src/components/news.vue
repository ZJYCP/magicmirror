<template>
    <div id="news">
        <swiper v-if="showFlag" :options="swiperOption" class="newsSwiper">
            <swiperSlide v-for="news in newsList" :key="news">
                <p>{{news}}</p>
            </swiperSlide>
        </swiper>
    </div>
</template>

<script>
    import moment from 'moment'
    import {swiper, swiperSlide} from 'vue-awesome-swiper'

    export default {
        name: "news",
        components: {
            swiper,
            swiperSlide
        },

        data() {
            return {
                newsList: [],
                showFlag:false,
                swiperOption: {
                    direction: 'vertical',
                    loop: true,
                    autoHeight: true,
                    speed: 700,
                    on: {
                        init() {
                            let _this = this
                            setInterval(() => {
                                _this.slideNext()
                            }, 5000)
                        }
                    }
                }
            }
        },
        methods: {
            async getNews() {
                this.newsList = []
                let start = parseInt(moment().format('h')) * 10  //以当前时间为一个计算值开始
                let res = await this.$http.get(`/news/get?channel=新闻&start=${start}&num=10&appkey=31c6d5efb47bb0ef`)
                let data = res.result.list
                console.log('新闻信息',data);
                this.showFlag=true
                data.forEach((item) => {
                    this.newsList.push(item.title)
                })
            },

        },
        mounted() {
            // 每隔一个小时拉取新的新闻
            this.getNews()
            setInterval(()=>{
                this.getNews()
            },1000*60*60)
        }
    }
</script>

<style scoped lang="scss">
    #news{
        width: 100%;
    }

    p {
        font-size: .39rem;
        text-align: center;
    }

    .newsSwiper {
        height: .5rem;
    }

</style>
