<script> 
export default {
  data() {
    return {
      page: 1,
      itemsPerPage: 20,
      itemsTotal: 300
    }
  }
}
</script>


<template>
  <div style="margin: auto" class="center">
    <div style="text-align: center">
      <h1>Search for the Inscription here</h1>
    </div>

    <div style="padding-left: 20%; padding-right: 20%">
      <i-input placeholder="Enter Script ID...">
        <template #append>
          <i-button color="primary">
            <i-icon name="ink-search" />
          </i-button>
        </template>
      </i-input>

      <i-table striped style="padding-top: 3rem">
        <thead>
          <tr>
            <th>Script ID</th>
            <th>Text</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">M-1892</th>
            <td><div class="cell"><a class="indus_text"> &#xE04D &#xE041 &#xE065 &#xE065 &#xE07B &#xE07B &#xE046 &#xE06E &#xE05E &#xE01C </a> </div></td>
          </tr>
          <tr>
            <th scope="row">H-270</th>
            <td><a class="indus_text"> &#xe5a5; &#xe2de; &#xe2c9; &#xe33a; &#xe61b; &#xe4eb; &#xe3fe; &#xe165;</a></td>
          </tr>
          <tr>
            <th scope="row">H-10</th>
            <td><a class="indus_text">&#xe2c9; &#xe61b; &#xe36f; &#xe321; &#xe5da;</a></td>
          </tr>
          <tr>
            <th scope="row">H-11</th>
            <td><a class="indus_text">&#xe06c; &#xe61b; &#xe12f; &#xe122; &#xe2c9; &#xe6e8;</a></td>
          </tr>
          <tr>
            <th scope="row">H-12</th>
            <td><a class="indus_text">&#xe396; &#xe321; &#xe5dc; &#xe115; &#xe10a; &#xe2d7; &#xe708;</a></td>
          </tr>
          <tr>
            <th scope="row">H-13</th>
            <td><a class="indus_text">&#xe61b; &#xe046; &#xe22a; &#xe2d7; &#xe709;</a></td>
          </tr>
          <tr>
            <th scope="row">H-14</th>
            <td><a class="indus_text">&#xe61b; &#xe3db; &#xe627; &#xe2cb; &#xe346;</a></td>
          </tr>
        </tbody>
      </i-table>

      <i-pagination v-model="page" :items-total="itemsTotal" :items-per-page="itemsPerPage" />
    </div>
  </div>
</template>

<style>
.center {
  float: center;
  justify-content: center;
}

.indus_text {
  font-family: indus;
  font-size: 25px;
}

.cell {
  width: 50%;
  float: center;
}
</style>
