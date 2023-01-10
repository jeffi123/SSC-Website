

<script lang="ts">
import { defineComponent, inject, ref } from 'vue';

import IconMoon from '~icons/fa-solid/moon'
import IconSun from '~icons/fa-solid/sun'

export default defineComponent({
  setup () {
    const inkline = inject<Prototype>('inkline', {} as any);
    const colorMode = ref(inkline.options.colorMode);

    // Set the initial color mode value to determine the icon to be displayed
    if (colorMode.value === 'system' && typeof window !== 'undefined') {
      colorMode.value = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    // Toggle between light and dark mode
    const toggleColorMode = () => {
      const mode = colorMode.value === 'dark' ? 'light' : 'dark';

      inkline.options.colorMode = mode;
      colorMode.value = mode;
    };

    return {
      colorMode,
      toggleColorMode,
    };
  }
});

</script>

<template>
<i-navbar>
    <i-navbar-brand to="/">
        <img v-if="colorMode === 'dark'" src="../assets/Logo-White.svg" style="width: 70px; height: 70px" >
        <img v-else src="../assets/Logo-Black.svg" style="width: 70px; height: 70px" >
    </i-navbar-brand>
    <i-navbar-collapsible>
        <i-nav>
            <i-nav-item to="/">
                Home
            </i-nav-item>
            <i-nav-item to="/about">
                About
            </i-nav-item>
            <i-nav-item to="/contact">
                Contact
            </i-nav-item>
						<i-nav-item @click="toggleColorMode" >
								<icons-fas-moon v-if="colorMode === 'light'" size="20px"/>
								<icons-fas-sun v-else size="20px"/>
						</i-nav-item>
        </i-nav>
        <i-input placeholder="Type something..">
            <template #append>
                <i-button color="primary">
                    <i-icon name="ink-search" />
                </i-button>
            </template>
        </i-input>
    </i-navbar-collapsible>
</i-navbar>

</template>

<!-- <style > -->
<!-- @import '@inkline/inkline/css/mixins'; -->
<!-- .navbar { -->
<!--     --navbar--light--background: var(--color-white); -->
<!--     --navbar--light--item--background: var(--color-white); -->
<!--     --navbar--light--item--hover--background: var(--color-light); -->
<!--     --navbar--light--collapsed--background: transparent; -->
<!---->
<!--     --navbar--dark--collapsed--background: transparent; -->
<!---->
<!--     @include breakpoint-down('md') { -->
<!--         .nav.navbar-icons { -->
<!--             display: flex; -->
<!--             flex-direction: row; -->
<!--             justify-content: space-between; -->
<!--             margin-top: var(--margin-top); -->
<!--             margin-bottom: var(--margin-bottom); -->
<!--             .nav-item { -->
<!--                 width: auto; -->
<!--             } -->
<!--         } -->
<!--         .button { -->
<!--             margin-left: 0; -->
<!--             width: 100%; -->
<!--         } -->
<!--     } -->
<!-- } -->
<!-- </style> -->
