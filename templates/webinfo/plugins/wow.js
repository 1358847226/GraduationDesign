import Vue from 'vue';
import { WOW } from 'wowjs'

window.WOW = WOW;  //因为服务端没有window，而wowjs里面是有window的，所以这里必须手动创建一个
Vue.prototype.$wow = new WOW()
