<template>
  <v-container>
    {{ ddd }}
    <v-row justify="center">
      <v-col v-for="deck in decks" :key="deck.name" cols="4">
        <NuxtLink
          :to="`/deck/${deck.id}`"
          style="text-decoration: none; color: inherit"
        >
          <v-card>
            <v-card-title class="text-center">
              {{ deck.name }}
            </v-card-title>
            <v-card-subtitle class="text-center">
              {{ deck.description }}
            </v-card-subtitle>
          </v-card>
        </NuxtLink>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";

interface Deck {
  id: number;
  name: string;
  description: string;
}

const { data: ddd } = await useFetch("http://localhost:8000/api/decks");

console.log(ddd._rawValue.decks);
const result: Deck[] = ddd._rawValue.decks;
const decks = ref<Deck[]>(result);
</script>
