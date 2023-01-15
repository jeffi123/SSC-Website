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
  <div style="margin: auto" class="center">
    <div style="text-align: center">
      <img
        src="../assets/Logo-White.svg"
        alt="Indus logo"
        class="logo -white"
        v-if="colorMode === 'dark'"
        style="width: 15%; height: auto"
      />
      <img
        src="../assets/Logo-Black.svg"
        alt="Indus logo"
        class="logo -black"
        style="width: 15%; height: auto"
        v-else
      />

      <h3><span>Sign in to continue</span></h3>
    </div>

    <div style="padding-left: 30%; padding-right: 30%; padding-top: 1rem;">
      <i-form>
        <i-form-group>
          <i-input
            id="email1"
            v-model="email"
            type="text"
            placeholder="Email"
          />
        </i-form-group>

        <i-form-group>
          <i-input
            id="password1"
            type="password"
            v-model="password"
            placeholder="Password"
            :toggleMask="true"
            inputClass="w-full"
            inputStyle="padding:1rem"
          />
        </i-form-group>
        <i-form-group style="margin-top: 5rem;">
          <i-button type="submit" :loading="loading"> Submit </i-button>
        </i-form-group>
      </i-form>
    </div>
  </div>
</template>

<style lang="scss">
@import "@inkline/inkline/css/variables";
@import "@inkline/inkline/css/mixins";

.center {
  float: center;
  justify-content: center;
}

</style>
