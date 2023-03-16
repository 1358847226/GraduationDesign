export default function ({ $axios, redirect, app }) {
  $axios.onRequest((config) => {
    return new Promise((resolve, reject) => {
      const token = app.$cookies.get('token')
      if (token) {
        config.headers.Authorization = token
      }
      resolve(config)
    })
  })
  $axios.onResponse((res) => {
    return res.data
  })

  $axios.onError((error) => {
    const code = parseInt(error.response && error.response.status)
    if (code === 400) {
      alert('请求失败' + error)
    }
  })
}
