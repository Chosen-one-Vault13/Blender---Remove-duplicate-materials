# Blender-remove-duplicate-materials
Remap materials with duplicates ending in .001,.002 etc. and purges the duplicated materials
Once you install the add-on you can find the command via search menu, look for "Remove Duplicate Materials". It should then automatically remap all the duplicated materials (provided the duplicates are named like <materialname>.0xx) and then purge the unused materials.

IMPORTANT: 

<ul>
  <li>Make sure you have backups of your Blender file in case a material is deleted accidentally.</li>
  <li>For your main materials (the ones that you don't want to be purged) make sure their names are not ending with .001,.002 and so on, otherwise they will be deleted even if there no duplicates.</li>
  <li>The add-on does affect Worlds, only Materials.</li>
  <li>If the duplicated material is not assigned to any object prior to running then it will not be deleted. Clicking on purge inside Blender should take care of these materials.</li>
</ul>

  
 
.
