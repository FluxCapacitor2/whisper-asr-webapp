<!--
    @component
    A carbon copy of Vercel's [Geist loading spinner](https://vercel.com/design/spinner), because I really like the way it looks.
    
    Side note: Who made it first, Vercel or [this website](https://loading.io/css)?
-->
<script lang="ts">
  export let size = 48;
  export let color = "#8f8f8f";
  export let elements = 12;
  const arr = Array.from({ length: elements }).fill(undefined);
</script>

<div
  class="spinner-wrapper"
  style="--size: {size}px; --elements: {elements}; --spinner-color: {color};"
>
  <div class="spinner">
    {#each arr as _, i}
      <div style="--nth-child: {i};" />
    {/each}
  </div>
</div>

<style lang="postcss">
  .spinner-wrapper,
  .spinner {
    width: var(--size);
    height: var(--size);
  }
  .spinner {
    position: relative;
    top: 50%;
    left: 50%;
  }
  .spinner div {
    background-color: var(--spinner-color);

    animation: loader-pulse calc(var(--elements) * 0.1s) linear infinite;
    border-radius: 5px;

    height: 8%;
    left: -10%;
    position: absolute;
    top: -3.9%;
    width: 24%;

    transform: rotate(calc((360deg / var(--elements)) * var(--nth-child)))
      translate(146%);
    animation-delay: calc((var(--elements) - var(--nth-child)) * -0.1s);
  }
  @keyframes loader-pulse {
    0% {
      opacity: 1;
    }
    to {
      opacity: 0.15;
    }
  }
</style>
