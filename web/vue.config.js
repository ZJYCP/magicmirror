module.exports = {
    devServer: {
        open: false,
        host: '',
        port: 8080,
        https: false,
        hotOnly: false,
        disableHostCheck: true,
        proxy: {
            '/api': {
                target: 'https://api.jisuapi.com',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '/'
                }
            }
        },

        before: app => {
        }
    },
}
