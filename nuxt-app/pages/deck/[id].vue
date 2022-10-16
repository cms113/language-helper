<template>
  <v-container>
    <v-row v-if="pending" justify="center">
      <v-progress-circular indeterminate size="50" color="blue" />
    </v-row>
    <v-row v-else align="center" justify="center">
      <v-col cols="auto">
        <v-card
          width="400px"
          rounded="lg"
          color="#1F7087"
          theme="dark"
          id="card"
        >
          <v-card-title class="text-center text-h4 my-2">
            {{ currentCard.question }}
          </v-card-title>
          <v-img
            v-if="currentCard.imageURL"
            width="100%"
            aspect-ratio="1"
            :src="currentCard.imageURL"
          />
          <v-card-text>
            <v-form ref="form" lazy-validation v-model="valid">
              <v-text-field
                v-model="currentCard.response"
                theme="default"
                placeholder="Answer here!"
                :rules="[
                  (v) =>
                    v.toLowerCase() === currentCard.translation.toLowerCase() ||
                    'Not quite!',
                ]"
                @input="form.resetValidation()"
              />
            </v-form>
          </v-card-text>

          <v-card-actions>
            <v-row justify="center">
              <v-btn
                variant="outlined"
                @click="checkAnswer"
                width="150px"
                color="white"
              >
                Submit
              </v-btn>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed, ref, nextTick } from "vue";
const { $unsplash } = useNuxtApp();
const form = ref(null);
const route = useRoute();
const id = route.params.id;

const { pending, data: cards } = useLazyFetch(
  `http://localhost:8000/api/deck/${id}`
);

const index = ref(0);
const valid = ref(false);

const currentCard = computed(() => {
  if (pending.value === true) {
    return null;
  }
  return cards.value[index.value];
});

watch(currentCard, async (newVal) => {
  if (currentCard.value?.imageURL === "") {
    currentCard.value.imageURL = await getImage();
    await saveCardStatus(index.value);
  }
});

function nextCard() {
  const card = document.getElementById("card");
  card.classList.add("fade-out");
  setTimeout(addNextCard, 1000);
}

function addNextCard() {
  index.value++;
  nextTick(() => {
    const card = document.getElementById("card");
    card.classList.remove("fade-out");
  });
}

function checkAnswer() {
  var valid = form.value.validate();
  if (valid) {
    currentCard.value.dateAnsweredCorrectly = new Date();
    saveCardStatus(index.value);
    nextCard();
  }
}

async function getImage() {
  try {
    var keyword = currentCard.value.question;
    var photos = await $unsplash.search.getPhotos({ query: keyword });
    return photos.response.results[0].urls.full;
  } catch (err) {
    console.log(err);
  }
}

async function saveCardStatus(index) {
  var cardToSave = cards.value[index];
  try {
    await $fetch(`http://localhost:8000/api/card`, {
      method: "PATCH",
      body: {
        card: cardToSave,
      },
    });
  } catch (err) {
    console.log(err);
  }
}
</script>

<style scoped>
.fade-out {
  animation: fade 1s;
  -moz-animation: fade 1s; /* Firefox */
  -webkit-animation: fade 1s; /* Safari and Chrome */
}

@keyframes fade {
  from {
    opacity: 1;
    transform: translate(0, 0);
  }
  to {
    opacity: 0;
    transform: translate(50px, 50px);
  }
}
@-moz-keyframes fade {
  from {
    opacity: 1;
    transform: translate(0, 0);
  }
  to {
    opacity: 0;
    transform: translate(50px, 50px);
  }
}
@-webkit-keyframes fade {
  from {
    opacity: 1;
    transform: translate(0, 0);
  }
  to {
    opacity: 0;
    transform: translate(50px, 50px);
  }
}
</style>
