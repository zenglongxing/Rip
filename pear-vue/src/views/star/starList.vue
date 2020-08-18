<template>
    <div>
        <a-row :gutter="24">
            <a-col :span="6" v-for="star in stars" :key="star.id">
                <a-card hoverable style="width: 300px" class="star-card" @click="go_movie(star.id)">
                    <img
                    slot="cover"
                    :alt="star.actor_name"
                    :src="star.online_photo"
                    />
                    <a-card-meta :title="star.actor_name" :description="star.new_movie_name">
                    </a-card-meta>
                </a-card>
            </a-col>
        </a-row>
        <a-spin :spinning="!scrollFlag" class="spin-c"/>
        <a-back-top class="ant-back-top">
            <div class="ant-back-top-inner">
                UP
            </div>
        </a-back-top>
    </div>
</template>
<script>
import {ListMixin} from '@/mixins/ListMixin'
import {getStar} from '@api/api'

export default {
    name: "starList",
    mixins: [ListMixin],
    data() {
        return {
            stars: [],
            pageSize: 12,
            currPage: 1,
            scrollFlag: false,
            noMore: false
        }
    },
    mounted() {
        window.addEventListener('scroll', this.handleScroll)
    },
    created() {
        this.infinite()
    },
    methods: {
        handleScroll() {
            if ((document.documentElement.scrollTop + window.innerHeight) >= document.getElementsByClassName('container').item(0).offsetHeight - 20) {
                if (this.scrollFlag && !this.noMore) {
                    this.scrollFlag = false
                    this.infinite()
                }
            }
        },
        infinite() {
            let that = this
            getStar({pageSize: that.pageSize, currPage: that.currPage}).then((res) => {
                if (res.success) {
                    if (that.stars.length > 0) {
                        that.stars = that.stars.concat(res.data.results)
                    } else {
                        that.stars = res.data.results
                    }
                    if (res.data.next) {
                        that.currPage += 1
                    } else {
                        this.noMore = true
                    }
                }
                this.scrollFlag = true
            })
        },
        go_movie(satrId) {
            this.$router.push({
                name: "movie",
                params: {
                    starId: satrId
                }
            })
        }
    }
}
</script>

<style scoped>
    .star-card {
        height: 450px;
    }

    .spin-c {
        position: absolute;
        width: 100%;
        bottom: 0;
        padding: 0 16px;
        margin: 48px 0 24px;
        text-align: center;
    }

    .ant-back-top {
        bottom: 100px;
    }

    .ant-back-top-inner {
        height: 40px;
        width: 40px;
        line-height: 40px;
        border-radius: 4px;
        background-color: #1088e9;
        color: #fff;
        text-align: center;
        font-size: 20px;
    }
</style>
