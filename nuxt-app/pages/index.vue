<template>
  <v-container>
    <v-row v-if="pending" justify="center">
      <v-progress-circular indeterminate size="50" color="blue" />
    </v-row>
    <v-row v-else justify="center">
      <v-col v-for="deck in decks" :key="deck.id" cols="4">
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
import { ref } from "vue";

interface Deck {
  id: number;
  name: string;
  description: string;
}

const { pending, data: decks } = useLazyFetch(
  "http://localhost:8000/api/decks"
);
</script>
