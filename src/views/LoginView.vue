<script lang="ts">
import { defineComponent, inject, ref } from "vue";

export default {
  setup() {
    const inkline = inject("inkline", {} as any);
    const colorMode = ref(inkline.options.colorMode);

    // Set the initial color mode value to determine the icon to be displayed
    if (colorMode.value === "system" && typeof window !== "undefined") {
      colorMode.value = window.matchMedia("(prefers-color-scheme: dark)")
        .matches
        ? "dark"
        : "light";
    }

    return {
      colorMode,
    };
  },
  data() {
    return {
      email: "",
      password: "",
      checked: false,
    };
  },
};
</script>

<template>
  <img
    src="../assets/Logo-White.svg"
    alt="Indus logo"
    class="logo -white"
    v-if="colorMode === 'dark'"
    style="width: 81px; height: 60px"
  />
  <img
    src="../assets/Logo-Black.svg"
    alt="Indus logo"
    class="logo -black"
    v-else
    style="width: 81px; height: 60px"
  />
  <div>Welcome!</div>
  <span>Sign in to continue</span>
  <i-input
    id="email1"
    v-model="email"
    type="text"
    placeholder="Email"
    style="padding: 1rem"
  />

  <i-input
    id="password1"
    type="password"
    v-model="password"
    placeholder="Password"
    :toggleMask="true"
    inputClass="w-full"
    inputStyle="padding:1rem"
  />
  <i-button label="Sign In"></i-button>
</template>

<style lang="scss"></style>