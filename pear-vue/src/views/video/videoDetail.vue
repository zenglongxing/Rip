<template>
    <div style="padding: 20px">
        <a-descriptions
                title="影片介绍"
                bordered
                :column="{ xxl: 4, xl: 3, lg: 3, md: 3, sm: 2, xs: 1 }"
        >
            <a-descriptions-item label="名称">
                {{movieInfo.name}}
            </a-descriptions-item>
            <a-descriptions-item label="简介">
                {{movieInfo.describe}}
            </a-descriptions-item>
            <a-descriptions-item label="导演">
                {{movieInfo.director}}
            </a-descriptions-item>
            <a-descriptions-item label="番号">
                {{movieInfo.fan_num}}
            </a-descriptions-item>
            <a-descriptions-item label="标签">
                {{movieInfo.labels}}
            </a-descriptions-item>
            <a-descriptions-item label="上线时间">
                {{movieInfo.new_cloud_time}}
            </a-descriptions-item>
            <a-descriptions-item label="发行时间">
                {{movieInfo.push_time}}
            </a-descriptions-item>
            <a-descriptions-item label="评分">
                {{movieInfo.score}}
            </a-descriptions-item>
            <a-descriptions-item label="女优">
                <a v-for="(item,index) in movieInfo.star" :key="index" onclick="go_actor()">{{item.actor_name}}</a>
            </a-descriptions-item>
        </a-descriptions>
        <a-row :gutter="24">
            <a-col :span="4" v-for="(item,index) in images" :key="index">
                <!--<img :src="item.path" :preview="index" :alt="movieInfo.name" width="300" height="400"/>-->
            </a-col>
        </a-row>
            <video-player class="video-player vjs-custom-skin"
                          ref="videoPlayer"
                          :playsinline="true"
                          :options="playerOptions"
                          @ready="playerReadied"
                          @loadeddata="onPlayerLoadeddata($event)"
                          @canplay="onPlayerCanplay($event)"
                          @canplaythrough="onPlayerCanplaythrough($event)"
                          @play="onPlayerPlay($event)"
                          @playing="onPlayerPlaying($event)"
                          @timeupdate="onPlayerTimeupdate($event)"
                          @pause="onPlayerPause($event)"
                          @waiting="onPlayerWaiting($event)"
                          @ended="onPlayerEnded($event)"
                          @statechanged="playerStateChanged($event)"
            ></video-player>
    </div>
</template>

<script>
import {getAction} from "../../api/manage";

export default {
    name: "videoDetail",
    data() {
        return {
            movieId: '',
            images: [],
            movieInfo: {},
            playerOptions: {
                playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                autoplay: false, //如果true,浏览器准备好时开始回放。
                muted: false, // 默认情况下将会消除任何音频。
                loop: false, // 导致视频一结束就重新开始。
                // preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                language: 'zh-CN',
                aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                // techOrder: ['html5','flash'],//设置顺序，
                flash: {
                    hls: {
                        withCredentials: false
                    }
                }
                ,
                html5: {
                    hls: {
                        withCredentials: false
                    }
                }
                ,
                hls: true,
                sources:
                    [{
                        type: "video/mp4",//这里的种类支持很多种：基本视频格式、直播、流媒体等，具体可以参看git网址项目
                        src: '' //url地址
                    }],
                poster: "", //你的封面地址
                // width: document.documentElement.clientWidth, //播放器宽度
                notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                controlBar: {
                    timeDivider: true,
                    durationDisplay: true,
                    remainingTimeDisplay: false,
                    fullscreenToggle: true  //全屏按钮
                }
            }
        }
    },
    created() {
        this.getMovieId()
        this.getVideoPath()
        this.getImgs()
        this.getMovieInfo()
    },
    computed: {
        player() {
            return this.$refs.videoPlayer.player;
        }
    },
    methods: {
        getImgs() {
            getAction('/photo/', {'video': this.movieId}).then((res) => {
                if (res.success) {
                    this.images = res.data
                }
            })
        },
        getMovieId() {
            this.movieId = this.$route.params.movieId;
        },
        getMovieInfo() {
            getAction('/movie/', {'id': this.movieId}).then((res) => {
                if (res.success) {
                    this.movieInfo = res.data[0]
                }
            })
        },
        go_actor() {

        },
        getVideoPath() {
            getAction('/videoPath/', {'videoId': this.movieId}).then((res) => {
                if (res.success) {
                    this.playerOptions.sources[0].src = res.data.full_path_url
                    this.playerOptions.poster = res.data.thumbnail
                }
            })
        }, initPlay(player) {
            console.log('initPlay>当前视频播放器实例对象', this.player);
            player.play();
        },

        /* 视频播放 */
        // 视频准备完毕
        playerReadied(player) {
            console.log('Readied>视频准备完毕!', player);
        },

        // 视频加载完成
        onPlayerLoadeddata(player) {
            this.spinning = false
            console.log('Loadeddata>视频加载完成!', player);
        },

        // 可以播放视频
        onPlayerCanplay(player) {
            console.log('Canplay>可以播放视频!', player);
            this.spinning = false
        },

        // 拖动视频条会触发事件-视频暂停>可以播放视频>可以播放视频至拖动位置>视频播放>视频加载中>可以播放视频>视频播放中>视频加载中>可以播放视频>视频播放中>视频加载中>可以播放视频>视频播放中>可以播放视频至拖动位置
        // 可以播放视频至拖动位置
        onPlayerCanplaythrough(player) {
            console.log('Canplaythrough>可以播放视频至拖动位置!', player);
        },

        // 视频播放
        onPlayerPlay(player) {
            console.log('Play>视频播放!', player);
        },

        // 视频播放中
        onPlayerPlaying(player) {
            console.log('Playing>视频播放中!', player);
        },

        // 视频时间更新中
        onPlayerTimeupdate(player) {
            // console.log('Timeupdate>视频时间更新中!', player);
        },

        // 视频暂停
        onPlayerPause(player) {
            console.log('Pause>视频暂停!', player);
        },

        // 视频加载中
        onPlayerWaiting(player) {
            console.log('Waiting>视频加载中!', player);
            this.spinning = true
        },

        // 视频状态改变
        playerStateChanged(playerCurrentState) {
            console.log('StateChanged>视频状态改变', playerCurrentState);
        },

        // 视频播放结束
        onPlayerEnded(player) {
            console.log('Ended>视频播放结束!', player);
        }
    }
}
</script>

<style lang="scss">

</style>
