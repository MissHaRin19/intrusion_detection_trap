for file in ~/honeytoken/real/*; do
  if [[ -f "$file" && ! -L "$file" ]]; then
    if [[ ! -e "${file}.bak" ]]; then
      mv "$file" "${file}.bak"  
    fi
    ln -s ~/honeytoken/fake/data.txt "$file"  
  fi
done