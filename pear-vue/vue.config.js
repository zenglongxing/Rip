const path = require('path')

function resolve(dir) {
    return path.join(__dirname, dir)
}

module.exports = {
    css: {
        loaderOptions: {
            less: {
                lessOptions: {
                    modifyVars: {
                        'primary-color': '#1DA57A',
                        'link-color': '#1DA57A',
                        'border-radius-base': '2px',
                    },
                    javascriptEnabled: true,
                },
            },
        },
    },
    chainWebpack: (config) => {
        config.resolve.alias
            .set('@$', resolve('src'))
            .set('@api', resolve('src/api'))
            .set('@assets', resolve('src/assets'))
            .set('@comp', resolve('src/components'))
            .set('@views', resolve('src/views'))
            .set('@layout', resolve('src/layout'))
            .set('@static', resolve('src/static'))
            .set('node_modules', resolve('node_modules')),
            config.module
                .rule('swf')
                .test(/\.swf$/)
                .use('url-loader')
                .loader('url-loader')
                .options({
                    limit: 10000
                })
    },
    devServer: {
        port: 6941,
        proxy: {
            '/pear': {
                target: 'http://localhost:8000', //请求本地 需要jeecg-boot后台项目
                ws: false,
                changeOrigin: true
            },
        }
    },
};
