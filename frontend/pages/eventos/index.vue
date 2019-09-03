<template>
  <v-card>
    <v-simple-table>
      <thead>
        <tr>
          <th class="text-center">#</th>
          <th class="text-center">Materia - Projeto</th>
          <th class="text-center">Alunos</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in Projetos" :key="p.id">
          <td class="text-center">{{ p.id }}</td>
          <td class="text-center" v-if="p.materia == 1">Matematica - {{ p.descricao }}</td>
          <td class="text-center" v-else-if="p.materia == 2">Ciencias - {{ p.descricao }}</td>
          <td class="text-center" v-else>Not Found - {{ p.descricao }}</td>
          <td class="text-center"><v-btn :to="`/eventos/${p.id}/`" icon>Ver</v-btn></td>
        </tr>
      </tbody>
    </v-simple-table>
    
  </v-card>
</template>

<script>
export default {
  async asyncData({ $axios, params }) {
    try {
      let Projetos = await $axios.$get(`/projetos/`);

      return { Projetos };
    } catch (e) {
      return { Projetos: [] };
    }
  },
  data() {
    return {
      dialog: false,
      Projetos: [],
      search: "",
      headers: [
        {
          text: "id",
          align: "left",
          value: "id"
        },
        { text: "Evento", value: "evento", sortable: false },
        { text: "Partipcipante", value: "participante", sortable: false },
        { text: "Projeto", value: "descricao", sortable: false }
      ]
    };
  }
};
</script>