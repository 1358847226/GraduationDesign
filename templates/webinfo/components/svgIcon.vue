<template>
  <svg :class="svgClass" aria-hidden="true">
    <use :xlink:href="iconName"></use>
  </svg>
</template>

<script>
export default {
  name: 'SvgIcon',
  props: {
    iconClass: {
      type: String,
      required: true,
      default: ''
    },
    className: {
      type: String,
      default: ''
    }
  },
  computed: {
    iconName () {
      return `#icon-${this.iconClass}`
    },
    svgClass () {
      if (this.className) {
        return 'SvgIcon ' + this.className
      } else {
        return 'SvgIcon'
      }
    }
  }
}
</script>

<style scoped>
.SvgIcon {
  width: 100%;
  /*height: 1em;*/
  vertical-align: -0.15em;
  fill: none;
  overflow: hidden;
}
</style>
