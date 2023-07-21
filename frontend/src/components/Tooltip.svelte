<script lang="ts">
  export let tip: string;

  let hovered: boolean = false;
</script>

<div class="relative inline-block {hovered && 'z-50'}">
  <div
    role="tooltip"
    class="peer"
    on:mouseenter={() => (hovered = true)}
    on:mouseleave={() => setTimeout(() => (hovered = false), 150)}
  >
    <slot />
  </div>
  <p
    class="absolute w-96 max-w-[24rem] shadow-md bg-gray-100 dark:bg-gray-900 p-2 rounded-md invisible peer-hover:visible peer-hover:opacity-100 opacity-0 transition-all [text-transform:none] font-normal text-sm"
  >
    {tip}
  </p>
</div>
