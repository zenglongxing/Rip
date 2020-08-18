<template>
    <div>
        <a-back-top>
            <div class="ant-back-top-inner" title="回到顶部">
                UP
            </div>
        </a-back-top>
        <a-row :gutter="24">
            <a-col :span="12" v-for="movie in movies" :key="movie.id">
                <a-card hoverable class="star-card" @click="goVideo(movie.id,movie.name)">
                    <img
                            slot="cover"
                            :alt="movie.name"
                            :src="movie.photo"
                    />
                    <a-card-meta :title="movie.name" :description="movie.labels">
                        <div>
                            {{movie.score}},{{movie.labels}}
                        </div>
                    </a-card-meta>
                </a-card>
            </a-col>
        </a-row>
    </div>
</template>

<script>
import {getAction} from "../../api/manage";

export default {
    name: "movieList",
    data() {
        return {
            movies: [],
            starId: '',
        }
    }, methods: {
        getMovie() {
            this.starId = this.$route.params.starId
            let starId = this.starId;
            getAction('/movie/?ordering=-score', {'star': starId}).then((res) => {
                if (res.success) {
                    this.movies = res.data
                }
            })
        },
        goVideo(id, name) {
            this.$router.push({
                name: "video",
                params: {
                    movieId: id
                },
                meta: {title: name}
            })
        }
    },
    created() {
        this.getMovie()
    }
}
</script>

<style scoped>
    .star-card {
        height: 450px;
    }
</style>
