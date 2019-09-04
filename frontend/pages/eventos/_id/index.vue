<template>
  <v-card class="mx-auto">
    <v-card-title>{{ evento.descricao }}</v-card-title>

    <v-card-text>
      <h3>Projeto : {{ projeto.descricao }}</h3>
      <div v-for="p in participantes" :key="p.id">
          <h3>Alunos : {{ participantes.nome }}</h3>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  head() {
    return {
      title: "View Alunos"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let evento = await $axios.$get(`/eventos/${params.id}`);

      let projeto = await $axios.$get(`/projetos/${evento.projeto}`);

      let participanteProjeto = await $axios.$get(`/participantes-projetos/?evento=${params.id}`);

      let participantes = await $axios.$get(`/participantes/${participanteProjeto.participante}`);
      
      return { evento, projeto, participanteProjeto, participantes };
    } catch (e) {
      return { evento: [], projeto: [], participanteProjeto: [], participantes: [] };
    }
  },
  data() {
    return {
      evento: {
        descricao: "",
        projeto: ""
      },
      projeto: {
        id: "",
        descricao: ""
      },
      participanteProjeto: {
        id: "",
        participante: ""
      },
      participantes: {
        nome: ""
      }
    };
  }
};
</script>