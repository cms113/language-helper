<template>
  <div>
    <v-toolbar dense>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Learn Vocab</v-toolbar-title>

      <v-spacer></v-spacer>

      <NuxtLink to="/" style="text-decoration: none; color: inherit">
        <v-btn icon>
          <v-icon>mdi-home</v-icon>
        </v-btn>
      </NuxtLink>
    </v-toolbar>
    <slot />
  </div>
</template>
